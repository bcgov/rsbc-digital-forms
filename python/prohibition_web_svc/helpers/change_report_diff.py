"""
MV6020 change report diff.

Compares the parent revision of an MV6020 with its change report and reports
added, removed and modified records and fields. The police and ICBC copies of
a change report highlight these. Entity and involved person rows are matched by
the form's hidden row id (cr_row_id) when both revisions have it, so deleting a
row doesn't make the rows after it look changed.

    python -m python.prohibition_web_svc.helpers.change_report_diff before.json after.json
        [--config change_report_fields.json] [--out diff.json] [--strict] [--no-values]

Inputs are Form.io submissions ({"data": {...}}) or the bare data object.
--no-values drops old/new values so the output holds field paths only and is
safe to log. Never log the default output: values contain personal information.
"""
import argparse
import json
import os
import re
from datetime import datetime, timezone

DEFAULT_CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'change_report_fields.json')
ISO_DATETIME = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2}(\.\d+)?)?(Z|[+-]\d{2}:?\d{2})$')
NUMBER = re.compile(r'^-?\d+(\.\d+)?$')


def load_config(path=DEFAULT_CONFIG) -> dict:
    with open(path) as f:
        return json.load(f)


def _data(submission: dict) -> dict:
    return submission.get('data', submission) if isinstance(submission, dict) else {}


def _normalize(value):
    """Collapse representations Form.io treats as equal: empty values,
    numbers sent as strings, ISO datetimes in different offsets, and select
    options compared by their code."""
    if value is None or value == '' or value == {} or value == []:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        text = value.strip()
        if NUMBER.match(text):
            return float(text)
        if ISO_DATETIME.match(text):
            try:
                parsed = datetime.fromisoformat(text.replace('Z', '+00:00'))
                return parsed.astimezone(timezone.utc).isoformat()
            except ValueError:
                return text
        return text
    if isinstance(value, dict):
        if 'value' in value and 'label' in value:
            return _normalize(value['value'])
        return {k: _normalize(v) for k, v in value.items() if _normalize(v) is not None} or None
    if isinstance(value, list):
        return [_normalize(v) for v in value] or None
    return value


def _equal(a, b, strict: bool) -> bool:
    return a == b if strict else _normalize(a) == _normalize(b)


def _diff_fields(before: dict, after: dict, exclude, strict, skip=(), prefix='') -> list:
    changes = []
    for key in sorted(set(before) | set(after)):
        if key in exclude or key in skip:
            continue
        old, new = before.get(key), after.get(key)
        if not _equal(old, new, strict):
            changes.append({'path': prefix + key, 'old': old, 'new': new})
    return changes


def _usable_key(rows: list, key: str) -> bool:
    values = [row.get(key) for row in rows]
    return all(v not in (None, '') for v in values) and len(set(map(str, values))) == len(values)


def _match_key(before: list, after: list, keys: list):
    """First configured key whose values are present and unique on each side."""
    for key in keys:
        if _usable_key(before, key) and _usable_key(after, key):
            return key
    return None


def _person_pairs(before: list, after: list, config) -> tuple:
    """(match_by, [(old_index, new_index)]): by the form's row id when both revisions have one,
    else by position (revisions saved before the row id existed). None marks a missing side."""
    match_by = _match_key(before, after, config.get('person_match_keys', []))
    if not match_by:
        return 'position', [(i if i < len(before) else None, i if i < len(after) else None)
                            for i in range(max(len(before), len(after)))]
    new_index = {str(row.get(match_by)): i for i, row in enumerate(after)}
    old_keys = {str(row.get(match_by)) for row in before}
    pairs = [(i, new_index.get(str(row.get(match_by)))) for i, row in enumerate(before)]
    pairs += [(None, i) for i, row in enumerate(after) if str(row.get(match_by)) not in old_keys]
    return match_by, pairs


def _diff_involved_persons(before: list, after: list, config, strict, prefix) -> list:
    """Persons are matched by the form's row id (cr_row_id), or by position for older revisions.

    Each record has old_index / new_index (None when that side has no such person)."""
    exclude = set(config.get('exclude_in_involved_persons', []))
    match_by, pairs = _person_pairs(before, after, config)
    records = []
    for old_index, new_index in pairs:
        row = after[new_index] if new_index is not None else before[old_index]
        key = row.get(match_by) if match_by != 'position' else (new_index if new_index is not None else old_index)
        path = f'{prefix}involved_persons[{key}]' if match_by == 'position' else f'{prefix}involved_persons[{match_by}={key}]'
        record = {'path': path, 'old_index': old_index, 'new_index': new_index}
        if old_index is None:
            records.append({**record, 'change': 'added', 'new': after[new_index]})
        elif new_index is None:
            records.append({**record, 'change': 'removed', 'old': before[old_index]})
        else:
            fields = _diff_fields(before[old_index], after[new_index], exclude, strict, prefix=path + '.')
            if fields:
                records.append({**record, 'change': 'modified', 'fields': fields})
    return records


def _diff_entities(before: list, after: list, config, strict) -> list:
    exclude = set(config.get('exclude_in_entities', []))
    match_by = _match_key(before, after, config.get('entity_match_keys', []))
    if match_by:
        old_rows = {str(row.get(match_by)): row for row in before}
        new_rows = {str(row.get(match_by)): row for row in after}
    else:
        match_by = 'position'
        old_rows = {str(i): row for i, row in enumerate(before)}
        new_rows = {str(i): row for i, row in enumerate(after)}
    records = []
    for key in list(old_rows) + [k for k in new_rows if k not in old_rows]:
        path = f'entities[{match_by}={key}]'
        if key not in new_rows:
            records.append({'path': path, 'match_by': match_by, 'change': 'removed', 'old': old_rows[key]})
        elif key not in old_rows:
            records.append({'path': path, 'match_by': match_by, 'change': 'added', 'new': new_rows[key]})
        else:
            old, new = old_rows[key], new_rows[key]
            fields = _diff_fields(old, new, exclude, strict, skip={'involved_persons'}, prefix=path + '.')
            persons = _diff_involved_persons(old.get('involved_persons') or [], new.get('involved_persons') or [],
                                             config, strict, path + '.')
            if fields or persons:
                records.append({'path': path, 'match_by': match_by, 'change': 'modified',
                                'fields': fields, 'involved_persons': persons})
    return records


def _strip_values(node):
    if isinstance(node, list):
        return [_strip_values(n) for n in node]
    if isinstance(node, dict):
        return {k: _strip_values(v) for k, v in node.items() if k not in ('old', 'new')}
    return node


def diff(before_submission: dict, after_submission: dict, config: dict = None,
         strict: bool = False, include_values: bool = True) -> dict:
    config = config or load_config()
    before, after = _data(before_submission), _data(after_submission)
    exclude = set(config.get('exclude_top_level', []))
    fields = _diff_fields(before, after, exclude, strict, skip={'entities'})
    entities = _diff_entities(before.get('entities') or [], after.get('entities') or [], config, strict)
    result = {
        'summary': {
            'fields_modified': len(fields),
            'entities_added': sum(r['change'] == 'added' for r in entities),
            'entities_removed': sum(r['change'] == 'removed' for r in entities),
            'entities_modified': sum(r['change'] == 'modified' for r in entities),
            'unchanged': not fields and not entities,
            'mode': 'strict' if strict else 'normalized',
        },
        'fields': fields,
        'entities': entities,
    }
    return result if include_values else _strip_values(result)


def _show(value) -> str:
    if isinstance(value, dict) and 'label' in value:
        return str(value['label'])
    return json.dumps(value) if not isinstance(value, str) else repr(value)


def summarize(result: dict) -> str:
    s = result['summary']
    if s['unchanged']:
        return f"No changes ({s['mode']} comparison)."
    lines = [f"{s['fields_modified']} field(s) modified, {s['entities_added']} entity(ies) added, "
             f"{s['entities_removed']} removed, {s['entities_modified']} modified ({s['mode']} comparison)."]

    def field_line(f, indent):
        if 'old' in f or 'new' in f:
            return f"{indent}~ {f['path']}: {_show(f.get('old'))} -> {_show(f.get('new'))}"
        return f"{indent}~ {f['path']}"

    lines += [field_line(f, '  ') for f in result['fields']]
    for record in result['entities']:
        mark = {'added': '+', 'removed': '-', 'modified': '~'}[record['change']]
        lines.append(f"  {mark} {record['path']} {record['change']}")
        for f in record.get('fields', []):
            lines.append(field_line(f, '      '))
        for person in record.get('involved_persons', []):
            pmark = {'added': '+', 'removed': '-', 'modified': '~'}[person['change']]
            lines.append(f"      {pmark} {person['path']} {person['change']}")
            lines += [field_line(f, '          ') for f in person.get('fields', [])]
    return '\n'.join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description='Diff an MV6020 original and its change report.')
    parser.add_argument('before')
    parser.add_argument('after')
    parser.add_argument('--config', default=DEFAULT_CONFIG)
    parser.add_argument('--out', help='write the JSON diff here instead of stdout')
    parser.add_argument('--strict', action='store_true', help='compare raw values, no normalization')
    parser.add_argument('--no-values', action='store_true', help='omit old/new values (paths only)')
    args = parser.parse_args(argv)
    with open(args.before) as f:
        before = json.load(f)
    with open(args.after) as f:
        after = json.load(f)
    result = diff(before, after, load_config(args.config), args.strict, not args.no_values)
    output = json.dumps(result, indent=2, default=str)
    if args.out:
        with open(args.out, 'w') as f:
            f.write(output + '\n')
    else:
        print(output)
    print(summarize(result))


if __name__ == '__main__':
    main()
