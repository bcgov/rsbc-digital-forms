"""
MV6020 change report diff.

Compares the parent revision of an MV6020 with its change report and reports
added, removed and modified records and fields. The ICBC copy of a change
report highlights these.

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


def _diff_involved_persons(before: list, after: list, config, strict, prefix) -> list:
    """Involved persons have no stable id, so they are matched by position."""
    exclude = set(config.get('exclude_in_involved_persons', []))
    records = []
    for index in range(max(len(before), len(after))):
        path = f'{prefix}involved_persons[{index}]'
        if index >= len(before):
            records.append({'path': path, 'change': 'added', 'new': after[index]})
        elif index >= len(after):
            records.append({'path': path, 'change': 'removed', 'old': before[index]})
        else:
            fields = _diff_fields(before[index], after[index], exclude, strict, prefix=path + '.')
            if fields:
                records.append({'path': path, 'change': 'modified', 'fields': fields})
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
