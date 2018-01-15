import sys

from cerberus import Validator

FAIL_COUNT_MAX = 100

def validate(rows, schema):
    v = Validator(schema)
    line_count = 0
    fail_count = 0
    for row in rows:
        line_count += 1
        if not v.validate(row):
            errors = {
                'line': line_count,
                'error': v.errors,
                'row': row
            }
            print(errors)
            fail_count += 1
        if fail_count >= FAIL_COUNT_MAX:
            print('Too many errors. Stop validation.', file=sys.stderr)
            return fail_count
    return fail_count
