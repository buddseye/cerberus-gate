import pandas as pd
import yaml
import gzip


def check_delimiter(path):
    exts = path.split('.')
    if exts[-1] == 'csv':
        return ','
    elif exts[-1] == 'tsv':
        return '\t'
    elif exts[-1] == 'gz':
        if exts[-2] == 'csv':
            return ','
        elif exts[-2] == 'tsv':
            return '\t'
    if exts[-1] == 'gz':
        f = gzip.open(path, mode='rt')
    else:
        f = open(path)
    line = f.readline()
    if line.find('\t') == -1:
        return ','
    else:
        return '\t'


def readtable(table):
    pass


DEFAULT_NAN_LIST = [
    'NULL',
    '\\N',
]
def readfile(path, header=None, dtype=None, parse_dates=None, na_values=DEFAULT_NAN_LIST):
    delimiter = check_delimiter(path)
    f = pd.read_csv(path,
                    names=header,
                    sep=delimiter,
                    dtype=dtype,
                    na_values=na_values,
                    keep_default_na=False,
                    parse_dates=parse_dates,
                    iterator=True,
                    chunksize=100000)
    for df in f:
        for row in df.where(pd.notnull(df), None).itertuples():
            yield {col: getattr(row, col) for col in df}


def readschema(path):
    return yaml.load(open(path))


CERBERUS_TO_PANDAS_TYPE = {
    'boolean': 'bool',
    'binary': 'object',
    'date': 'str',
    'datetime': 'str',
    'dict': 'object',
    'float': 'float64',
    'integer': 'int64',
    'list': 'list',
    'number': 'float',
    'set': 'object',
    'string': 'str',
}
def dtype_from(cerberus_type):
    try:
        return CERBERUS_TO_PANDAS_TYPE[cerberus_type]
    except:
        return 'object'


def get_dtype(schema):
    dtypes = {}
    date_cols = []
    for key, value in schema.items():
        if 'type' not in value:
            continue
        dtypes[key] = dtype_from(value['type'])
        if value['type'] in ('date', 'datetime'):
            date_cols.append(key)
    return dtypes, date_cols
