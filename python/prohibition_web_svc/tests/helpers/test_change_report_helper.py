import copy
import re
from pathlib import Path
from jinja2 import ChainableUndefined, Environment, FileSystemLoader, select_autoescape
from python.prohibition_web_svc.helpers import change_report_helper

TEMPLATES = Path(__file__).resolve().parents[2] / 'templates'


def _entity(num, kind='V', label='VEHICLE', **fields):
    return {'entity_num': num, 'entity_type': {'value': kind, 'label': label},
            'surname': 'SAMPLE', 'involved_persons': [], **fields}


PARENT = {
    'collision_case_num': 'RZ001036',
    'street_on': 'MAIN ST',
    'total_est_damage': 18000,
    'hwy_route_num': {'code': '1', 'label': '1'},
    'entities': [
        _entity('01', estimated_vehicle_damage=10000,
                involved_persons=[{'status': 'driver', 'given_name': 'A'}, {'status': 'passenger', 'given_name': 'B'}]),
        _entity('30', 'P', 'PEDESTRIAN'),
    ],
}


def _change(**fields):
    data = copy.deepcopy(PARENT)
    data.update({'isChangeReport': True, 'parentRevision': 0, 'parentSubmissionId': 'a' * 24,
                 'parentFormId': 'b' * 24, 'reportType': 'change', 'collisionNumber': 'RZ001036'})
    data.update(fields)
    return data


def test_new_report_has_no_context():
    assert change_report_helper.build_context(copy.deepcopy(PARENT), PARENT) is None


def test_unchanged_change_report_has_nothing_to_highlight():
    context = change_report_helper.build_context(_change(), PARENT)
    assert context['highlights_available'] is True
    assert context['revision'] == 1 and context['parent_revision'] == 0
    assert context['changed'] == []
    assert context['summary']['unchanged'] is True


def test_changed_fields_are_listed_by_form_key():
    context = change_report_helper.build_context(_change(street_on='1ST AVE', total_est_damage='20500'), PARENT)
    assert context['changed'] == ['street_on', 'total_est_damage']


def test_numbers_sent_as_strings_are_not_changes():
    context = change_report_helper.build_context(_change(total_est_damage='18000'), PARENT)
    assert context['changed'] == []


def test_entity_changes_line_up_with_the_current_entities():
    entities = copy.deepcopy(PARENT['entities'])
    entities[0]['estimated_vehicle_damage'] = 12500
    entities[0]['involved_persons'][1]['given_name'] = 'C'
    entities.append(_entity('02'))
    context = change_report_helper.build_context(_change(entities=entities), PARENT)
    rows = context['entity_rows']
    assert len(rows) == 3
    assert rows[0]['change'] == 'modified'
    assert rows[0]['fields'] == ['estimated_vehicle_damage']
    assert rows[0]['persons'] == {1: {'change': 'modified', 'fields': ['given_name']}}
    assert rows[1]['change'] is None
    assert rows[2]['change'] == 'added'


def test_removed_entities_and_persons_are_reported():
    entities = [copy.deepcopy(PARENT['entities'][0])]
    entities[0]['involved_persons'] = entities[0]['involved_persons'][:1]
    context = change_report_helper.build_context(_change(entities=entities), PARENT)
    assert context['removed_entities'] == [{'entity_num': '30', 'entity_type': 'PEDESTRIAN'}]
    assert context['removed_persons'] == [{'entity_num': '01', 'persons': [2]}]


def test_change_report_fields_themselves_are_not_changes():
    context = change_report_helper.build_context(_change(parentRevision=3), dict(PARENT, isChangeReport=False))
    assert context['changed'] == []


def test_missing_parent_renders_without_highlights():
    for parent in (None, {}, 'not a dict'):
        context = change_report_helper.build_context(_change(), parent)
        assert context['highlights_available'] is False
        assert context['revision'] == 1
        assert [row['change'] for row in context['entity_rows']] == [None, None]


def test_parent_for_another_case_number_is_not_used():
    context = change_report_helper.build_context(_change(), dict(PARENT, collision_case_num='RZ999999'))
    assert context['highlights_available'] is False
    assert context['changed'] == []


def test_logs_counts_never_values(caplog):
    caplog.set_level('INFO')
    change_report_helper.build_context(_change(street_on='SECRET STREET'), PARENT)
    assert 'SECRET STREET' not in caplog.text
    assert 'MAIN ST' not in caplog.text


# --- mv6020.html, rendered with Jinja as render_with_playwright does (no browser) ---
# Real submissions fill every field the template reads; these fixtures don't, so
# missing fields render blank here (ChainableUndefined) instead of failing.

def _render(data):
    env = Environment(loader=FileSystemLoader(str(TEMPLATES)), autoescape=select_autoescape(['html', 'xml']),
                      undefined=ChainableUndefined)
    data = dict(data, print_options={'type': 'icbc', 'email': '', 'is_draft': False})
    return env.get_template('mv6020.html').render(data=dict(data, output_type='pdf'))


def _cell_classes(html, label):
    match = re.search(r'<div class="([^"]*)">\s*<label class="grid-label">' + re.escape(label), html)
    return match.group(1).split()


def test_template_highlights_changed_cells_only():
    data = _change(street_on='1ST AVE')
    data['change_report'] = change_report_helper.build_context(data, PARENT)
    html = _render(data)
    assert 'cr-changed' in _cell_classes(html, 'Collision Location - Street (ON)')
    assert 'cr-changed' not in _cell_classes(html, 'Collision Case No')
    assert 'revision 1, which replaces revision 0' in html
    assert 'are <span class="cr-changed cr-key">highlighted</span>' in html


def test_template_lists_removed_entities_and_marks_added_ones():
    data = _change(entities=[copy.deepcopy(PARENT['entities'][0]), _entity('02')])
    data['change_report'] = change_report_helper.build_context(data, PARENT)
    html = _render(data)
    assert 'Removed in this revision' in html
    assert 'Entity 30 (PEDESTRIAN)' in html
    assert html.count('Added in this revision') == 1


def test_template_says_when_highlights_are_unavailable():
    data = _change(street_on='1ST AVE')
    data['change_report'] = change_report_helper.build_context(data, None)
    html = _render(data)
    assert 'Changes could not be highlighted because revision 0 was not available' in html
    assert 'cr-changed' not in _cell_classes(html, 'Collision Location - Street (ON)')


def test_template_is_unchanged_for_new_reports():
    html = _render(copy.deepcopy(PARENT))
    assert 'CHANGE REPORT' not in html
    assert ' cr-changed' not in html.split('</style>', 1)[1]


def _all_cell_classes(html, label):
    """Classes of every cell with this label, in page order (police copy, then ICBC copy)."""
    pattern = r'<div class="([^"]*)">\s*<label class="grid-label">' + re.escape(label) + r'</label>'
    return [match.split() for match in re.findall(pattern, html)]


def _rendered_change(**changes):
    data = _change(**changes)
    data['change_report'] = change_report_helper.build_context(data, PARENT)
    return _render(data)


def test_template_highlights_entity_fields_on_their_entity_only():
    entities = copy.deepcopy(PARENT['entities'])
    entities[0]['estimated_vehicle_damage'] = 12500
    html = _rendered_change(entities=entities)
    # Entity 01 changed, entity 30 did not.
    assert ['cr-changed' in c for c in _all_cell_classes(html, 'Estimated Vehicle Damage ($)')] == [True, False]
    assert ['cr-changed' in c for c in _all_cell_classes(html, 'Entity Number')] == [False, False]


def test_template_highlights_person_fields_on_their_person_only():
    entities = copy.deepcopy(PARENT['entities'])
    entities[0]['involved_persons'][1]['age'] = 41
    html = _rendered_change(entities=entities)
    # Police copy "Box 14 Age" and ICBC copy "Box 14": person 1 unchanged, person 2 changed.
    assert ['cr-changed' in c for c in _all_cell_classes(html, 'Box 14 Age')] == [False, True]
    assert ['cr-changed' in c for c in _all_cell_classes(html, 'Box 14')] == [False, True]
    assert html.count('Changed in this revision') == 2  # entity heading and person heading


def test_template_highlights_every_cell_of_an_added_person():
    entities = copy.deepcopy(PARENT['entities'])
    entities[0]['involved_persons'].append({'status': 'passenger', 'given_name': 'C', 'surname': 'NEW'})
    html = _rendered_change(entities=entities)
    assert ['cr-changed' in c for c in _all_cell_classes(html, 'Box 14 Age')] == [False, False, True]
    assert ['cr-changed' in c for c in _all_cell_classes(html, 'Box 14')] == [False, False, True]
    assert 'Added in this revision' in html


def test_template_highlights_police_comments_and_witnesses():
    html = _rendered_change(police_comments='UPDATED', has_witnesses='Y',
                            witnesses=[{'witness_name': 'W', 'address': 'A', 'contact_phn_num': '1'}])
    assert all('cr-changed' in c for c in _all_cell_classes(html, 'Box 99 Police Comments'))
    assert 'cr-changed' in _all_cell_classes(html, 'Are there witnesses?')[0]
    assert re.search(r'<div class="grid-cell grid-cell-full cr-changed">\s*<table', html)


def test_template_highlights_box_fields_in_both_copies():
    html = _rendered_change(road_class={'value': '12', 'label': '12 TWO LANE'})
    assert all('cr-changed' in c for c in _all_cell_classes(html, 'Box 1 Road Class'))
    assert re.search(r'<div class="icbc-box cr-changed">\s*<div class="icbc-box-label">Box 1</div>', html)
