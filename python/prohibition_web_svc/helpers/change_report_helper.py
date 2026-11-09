"""
Change report context for the MV6020 police and ICBC copies.

A change report is a new revision of the same collision case number. The parent
revision arrives as payload.parentData: from Camunda (Form.io lookup) on
/api/v1/email, and from the form's pdfGenerator on /api/v1/print. This compares
it with the change report and tells the template what to highlight. The report
itself is always rendered in full.

Only the police and ICBC copies show the changes (BA, 2026-11-05); driver/entity
copies render as before. The context is built once per request and dropped at
render time for other copies (see context_for_copy), so the admin email and the
download-all zip, which render several copies from one payload, get it right.

The context added to the template data as data.change_report:

    parent_revision, revision   revision numbers (no branching: revision = parent + 1)
    highlights_available        False when the parent was missing or didn't match
    changed                     top-level form keys that changed, e.g. 'street_on'
    entity_rows                 one entry per current entity, in data.entities order:
                                {'change': 'added' | 'modified' | None, 'fields': [...],
                                 'persons': {index: {'change': ..., 'fields': [...]}},
                                 'deleted_persons': [{'index': parent index, 'person': parent row}]}
    removed_entities            parent entities missing from the change report
                                ({'entity_num', 'entity_type', 'index', 'entity': parent row})
    removed_persons             involved persons removed from an entity still present
    summary                     counts from the diff

For the police and ICBC copies, context_for_copy puts the deleted entities and
persons back into data.entities where they were, marked 'removed', so the
template shows them highlighted and crossed out. ICBC staff re-key changes from
the report, so a deletion has to be as visible as an edit. The saved data, the
totals and the ICBC payload never contain them.

Never log the diff itself: values hold personal information.
"""
import re
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.helpers import change_report_diff

logger = get_logger(__name__)

ENTITY_PATH = re.compile(r'^entities\[(?P<key>[a-z_]+)=(?P<value>[^\]]*)\]$')


HIGHLIGHTED_COPIES = ('police', 'icbc')


def is_change_report(data) -> bool:
    return isinstance(data, dict) and str(data.get('isChangeReport')).lower() == 'true'


def context_for_copy(template_data: dict) -> dict:
    """The template data for one copy.

    Police and ICBC copies get the deleted rows put back for display; other copies
    lose data.change_report. The input is not changed: one payload renders several copies.
    """
    if 'change_report' not in template_data:
        return template_data
    print_type = str(((template_data.get('print_options') or {}).get('type')) or '').lower()
    if print_type not in HIGHLIGHTED_COPIES:
        return {k: v for k, v in template_data.items() if k != 'change_report'}
    context = template_data['change_report']
    if not context or not context.get('highlights_available'):
        return template_data
    entities, rows = _with_deleted_rows(template_data.get('entities') or [], context)
    return {**template_data, 'entities': entities, 'change_report': {**context, 'entity_rows': rows}}


def _insert_at_old_positions(current: list, deleted: list) -> list:
    """current: [(item, meta)]; deleted: [(parent index, item, meta)]. Deleted items go back
    where they were in the parent, as far as the current list allows."""
    merged = list(current)
    for index, item, meta in sorted(deleted, key=lambda d: d[0]):
        merged.insert(min(index, len(merged)), (item, meta))
    return merged


def _deleted_meta(number) -> dict:
    return {'change': 'removed', 'fields': [], 'was_number': number}


def _with_persons(entity: dict, row: dict) -> tuple:
    persons = entity.get('involved_persons') or []
    current = [(person, row['persons'].get(i)) for i, person in enumerate(persons)]
    deleted = [(d['index'], d['person'], _deleted_meta(d['index'] + 1)) for d in row.get('deleted_persons', [])]
    merged = _insert_at_old_positions(current, deleted)
    entity = {**entity, 'involved_persons': [person for person, _ in merged]}
    row = {**row, 'persons': {i: meta for i, (_, meta) in enumerate(merged) if meta}}
    return entity, row


def _with_deleted_rows(entities: list, context: dict) -> tuple:
    current = [_with_persons(entity, row) for entity, row in zip(entities, context['entity_rows'])]
    deleted = []
    for removed in context.get('removed_entities', []):
        entity = removed.get('entity') or {}
        persons = entity.get('involved_persons') or []
        row = {**_deleted_meta(entity.get('entity_num')), 'deleted_persons': [],
               'persons': {i: _deleted_meta(i + 1) for i in range(len(persons))}}
        deleted.append((removed.get('index', len(entities)), entity, row))
    merged = _insert_at_old_positions(current, deleted)
    return [entity for entity, _ in merged], [row for _, row in merged]


def _parent_revision(data: dict):
    try:
        return int(data.get('parentRevision'))
    except (TypeError, ValueError):
        return None


def _field_name(path: str) -> str:
    return path.rsplit('.', 1)[-1]


def _row_index(rows: list, match_by: str, value: str):
    if match_by == 'position':
        index = int(value)
        return index if index < len(rows) else None
    return next((i for i, row in enumerate(rows) if str(row.get(match_by)) == value), None)


def _label(value) -> str:
    if isinstance(value, dict):
        return str(value.get('label') or value.get('value') or '')
    return '' if value is None else str(value)


def _entity_summary(row: dict, index=None) -> dict:
    return {'entity_num': row.get('entity_num'), 'entity_type': _label(row.get('entity_type')),
            'index': index, 'entity': row}


def _persons(record: dict) -> tuple:
    """({current index: change}, [deleted persons with their parent row])."""
    persons, deleted = {}, []
    for person in record.get('involved_persons', []):
        if person['change'] == 'removed':
            deleted.append({'index': person['old_index'], 'person': person['old']})
        else:
            persons[person['new_index']] = {
                'change': person['change'],
                'fields': sorted({_field_name(f['path']) for f in person.get('fields', [])})}
    return persons, deleted


def build_context(data: dict, parent_data) -> dict:
    """The data.change_report context for a change report, or None for a new report."""
    if not is_change_report(data):
        return None
    case_number = data.get('collision_case_num')
    parent_revision = _parent_revision(data)
    entities = data.get('entities') or []
    context = {
        'parent_revision': parent_revision,
        'revision': parent_revision + 1 if parent_revision is not None else None,
        'highlights_available': False,
        'changed': [],
        'entity_rows': [{'change': None, 'fields': [], 'persons': {}, 'deleted_persons': []} for _ in entities],
        'removed_entities': [],
        'removed_persons': [],
        'summary': None,
    }
    if not isinstance(parent_data, dict) or not parent_data:
        logger.warning(f'change report {case_number} has no parent data; the ICBC copy has no highlights')
        return context
    if str(parent_data.get('collision_case_num') or '').upper() != str(case_number or '').upper():
        logger.warning(f'change report {case_number}: the parent data is for another collision case number; '
                       f'the ICBC copy has no highlights')
        return context

    result = change_report_diff.diff(parent_data, data)
    parent_entities = parent_data.get('entities') or []
    context['highlights_available'] = True
    context['summary'] = result['summary']
    context['changed'] = sorted({f['path'] for f in result['fields']})
    for record in result['entities']:
        match = ENTITY_PATH.match(record['path'])
        if record['change'] == 'removed':
            old = record['old']
            index = next((i for i, row in enumerate(parent_entities) if row is old), None)
            context['removed_entities'].append(_entity_summary(old, index))
            continue
        index = _row_index(entities, match.group('key'), match.group('value'))
        if index is None:
            continue
        persons, deleted = _persons(record)
        context['entity_rows'][index] = {
            'change': record['change'],
            'fields': sorted({_field_name(f['path']) for f in record.get('fields', [])}),
            'persons': persons,
            'deleted_persons': deleted,
        }
        if deleted:
            context['removed_persons'].append({'entity_num': entities[index].get('entity_num'),
                                               'persons': [d['index'] + 1 for d in deleted]})
    logger.info(f"change report {case_number} revision {context['revision']}: "
                f"{result['summary']['fields_modified']} field(s) and "
                f"{len(result['entities'])} entity record(s) changed")
    return context
