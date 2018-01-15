import pandas
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


def readfile(path, header):
    delimiter = check_delimiter(path)
    f = pandas.read_csv(path,
                        names=header,
                        sep=delimiter,
                        iterator=True,
                        chunksize=100000)
    for df in f:
        for row in df.fillna('').itertuples():
            yield {col: getattr(row, col) for col in df}


def readschema(path):
    return yaml.load(open(path))
