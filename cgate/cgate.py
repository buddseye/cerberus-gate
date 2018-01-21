# -*- coding: utf-8 -*-

import sys
import argparse

from cgate.reader import readfile, readschema, get_dtype
from cgate.validation import validate

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', help='Table name or File path')
    parser.add_argument('--schema', '-s', help='Cerberus schema file')
    args = parser.parse_args()

    schema = readschema(args.schema)
    try:
        header = schema['header']
    except:
        header = None
    dtype, date_cols = get_dtype(schema['schema'])
    dfs = readfile(args.target, header=header, dtype=dtype, parse_dates=date_cols)
    fail_count = validate(dfs, schema['schema'])
    if fail_count != 0:
        print('Failed {0} error...'.format(fail_count), file=sys.stderr)
        return 1
    print('Success!', file=sys.stderr)
    return 0
