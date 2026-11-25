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
    assert context['removed_entities'] == [{'entity_num': '30', 'entity_type': 'PEDESTRIAN', 'index': 1,
                                            'entity': PARENT['entities'][1]}]
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

def _render(data, copy_type='icbc', **print_options):
    env = Environment(loader=FileSystemLoader(str(TEMPLATES)), autoescape=select_autoescape(['html', 'xml']),
                      undefined=ChainableUndefined)
    data = dict(data, print_options={'type': copy_type, 'email': '', 'is_draft': False, **print_options})
    # As the renderer does: per copy, deleted rows put back or the context dropped.
    data = change_report_helper.context_for_copy(dict(data, output_type='pdf'))
    return env.get_template('mv6020.html').render(data=data)


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
    # Police copy entity heading and the two ICBC copy entity headings.
    assert html.count('Added in this revision') == 3


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
    # Police copy entity and person headings, ICBC copy two entity headings and a person heading.
    assert html.count('Changed in this revision') == 5


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


# Deleted rows: matched by the form's row id, shown from the parent, highlighted and crossed out.

def _with_ids(entities):
    for e, entity in enumerate(entities):
        entity['cr_row_id'] = f'e{e}'
        for p, person in enumerate(entity['involved_persons']):
            person['cr_row_id'] = f'e{e}p{p}'
    return entities


PARENT_WITH_IDS = dict(PARENT, entities=_with_ids(copy.deepcopy(PARENT['entities'])))


def _deleting(edit):
    entities = copy.deepcopy(PARENT_WITH_IDS['entities'])
    edit(entities)
    data = _change(entities=entities)
    data['change_report'] = change_report_helper.build_context(data, PARENT_WITH_IDS)
    return data


def test_deleting_the_first_person_does_not_make_the_next_one_look_changed():
    data = _deleting(lambda entities: entities[0]['involved_persons'].pop(0))
    row = data['change_report']['entity_rows'][0]
    assert row['persons'] == {}
    assert row['deleted_persons'] == [{'index': 0, 'person': PARENT_WITH_IDS['entities'][0]['involved_persons'][0]}]
    assert data['change_report']['removed_persons'] == [{'entity_num': '01', 'persons': [1]}]


def test_older_revisions_without_row_ids_are_matched_by_position():
    entities = copy.deepcopy(PARENT['entities'])
    entities[0]['involved_persons'].pop(0)
    data = _change(entities=_with_ids(entities))
    row = change_report_helper.build_context(data, PARENT)['entity_rows'][0]
    assert row['persons'] == {0: {'change': 'modified', 'fields': ['given_name']}}  # status is not compared
    assert [d['index'] for d in row['deleted_persons']] == [1]


def test_renumbered_entity_is_matched_by_row_id():
    def delete_first_vehicle(entities):
        entities.insert(0, _entity('01', cr_row_id='new'))
        entities.pop(1)
    # The form renumbers: a vehicle deleted and another added gets the same entity number.
    context = _deleting(delete_first_vehicle)['change_report']
    assert [e['entity_num'] for e in context['removed_entities']] == ['01']
    assert context['entity_rows'][0]['change'] == 'added'


def test_police_and_icbc_copies_show_deleted_rows_where_they_were():
    data = _deleting(lambda entities: (entities[0]['involved_persons'].pop(0), entities.pop(1)))
    shown = change_report_helper.context_for_copy(dict(data, print_options={'type': 'police'}))
    assert [e['entity_num'] for e in shown['entities']] == ['01', '30']
    assert [p['given_name'] for p in shown['entities'][0]['involved_persons']] == ['A', 'B']
    rows = shown['change_report']['entity_rows']
    assert rows[0]['persons'] == {0: {'change': 'removed', 'fields': [], 'was_number': 1}}
    assert rows[1]['change'] == 'removed' and rows[1]['was_number'] == '30'
    # The payload itself is unchanged: it renders the other copies too.
    assert [e['entity_num'] for e in data['entities']] == ['01']
    assert len(data['entities'][0]['involved_persons']) == 1


def test_driver_copies_do_not_show_deleted_rows():
    data = _deleting(lambda entities: entities.pop(1))
    shown = change_report_helper.context_for_copy(dict(data, print_options={'type': 'entity', 'entity_num': '01'}))
    assert 'change_report' not in shown
    assert [e['entity_num'] for e in shown['entities']] == ['01']


def test_template_crosses_out_a_deleted_person_in_both_copies():
    html = _render(_deleting(lambda entities: entities[0]['involved_persons'].pop(0)))
    assert [('cr-deleted' in c, 'cr-changed' in c) for c in _all_cell_classes(html, 'Box 14 Age')] \
        == [(True, True), (False, False)]
    assert ['cr-deleted' in c for c in _all_cell_classes(html, 'Box 14')] == [True, False]
    assert html.count('Deleted in this revision (was Involved Person No. 1 in revision 0)') == 2


def test_template_crosses_out_a_deleted_entity_and_its_persons():
    html = _render(_deleting(lambda entities: entities.pop(0)))
    # Vehicle 01 (deleted, with its two persons) is shown before pedestrian 30.
    assert ['cr-deleted' in c for c in _all_cell_classes(html, 'Entity Number')] == [True, False]
    assert all('cr-deleted' in c for c in _all_cell_classes(html, 'Box 14 Age'))
    assert 'Deleted in this revision (was Entity No. 01 in revision 0)' in html
    assert '.cr-deleted .grid-input' in html
