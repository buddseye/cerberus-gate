# -*- coding: utf-8 -*-

import sys
import argparse

from cgate.reader import readfile, readschema
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
    rows = readfile(args.target, header=header)
    fail_count = validate(rows, schema['schema'])
    if fail_count != 0:
        print('Failed {0} error...'.format(fail_count), file=sys.stderr)
        return 1
    print('Success!', file=sys.stderr)
    return 0
