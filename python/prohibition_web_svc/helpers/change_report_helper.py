"""
Change report context for the MV6020 ICBC copy.

A change report is a new revision of the same collision case number. Camunda
reads the parent revision from Form.io and sends it as payload.parentData to
/api/v1/email. This compares it with the change report and tells the template
what to highlight. The report itself is always rendered in full.

The context added to the template data as data.change_report:

    parent_revision, revision   revision numbers (no branching: revision = parent + 1)
    highlights_available        False when the parent was missing or didn't match
    changed                     top-level form keys that changed, e.g. 'street_on'
    entity_rows                 one entry per current entity, in data.entities order:
                                {'change': 'added' | 'modified' | None, 'fields': [...],
                                 'persons': {index: {'change': ..., 'fields': [...]}}}
    removed_entities            parent entities missing from the change report
    removed_persons             involved persons removed from an entity still present
    summary                     counts from the diff

Never log the diff itself: values hold personal information.
"""
import re
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.helpers import change_report_diff

logger = get_logger(__name__)

ENTITY_PATH = re.compile(r'^entities\[(?P<key>[a-z_]+)=(?P<value>[^\]]*)\]$')
PERSON_PATH = re.compile(r'involved_persons\[(?P<index>\d+)\]$')


def is_change_report(data) -> bool:
    return isinstance(data, dict) and str(data.get('isChangeReport')).lower() == 'true'


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


def _entity_summary(row: dict) -> dict:
    return {'entity_num': row.get('entity_num'), 'entity_type': _label(row.get('entity_type'))}


def _persons(record: dict) -> tuple:
    persons, removed = {}, []
    for person in record.get('involved_persons', []):
        index = int(PERSON_PATH.search(person['path']).group('index'))
        if person['change'] == 'removed':
            removed.append(index + 1)
        else:
            persons[index] = {'change': person['change'],
                              'fields': sorted({_field_name(f['path']) for f in person.get('fields', [])})}
    return persons, removed


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
        'entity_rows': [{'change': None, 'fields': [], 'persons': {}} for _ in entities],
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
    context['highlights_available'] = True
    context['summary'] = result['summary']
    context['changed'] = sorted({f['path'] for f in result['fields']})
    for record in result['entities']:
        match = ENTITY_PATH.match(record['path'])
        if record['change'] == 'removed':
            context['removed_entities'].append(_entity_summary(record['old']))
            continue
        index = _row_index(entities, match.group('key'), match.group('value'))
        if index is None:
            continue
        persons, removed = _persons(record)
        context['entity_rows'][index] = {
            'change': record['change'],
            'fields': sorted({_field_name(f['path']) for f in record.get('fields', [])}),
            'persons': persons,
        }
        if removed:
            context['removed_persons'].append({'entity_num': entities[index].get('entity_num'), 'persons': removed})
    logger.info(f"change report {case_number} revision {context['revision']}: "
                f"{result['summary']['fields_modified']} field(s) and "
                f"{len(result['entities'])} entity record(s) changed")
    return context
