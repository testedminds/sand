import csv
from igraph import Graph as IGraph


def legalize(name):
    for c in r'[]/\;,><&*:%=+@!#^()|?^':
        name = name.replace(c, ' ')
    return name.replace(' ', '_').lower()


def write_file(f, data):
    with open(f, 'w') as result:
        result.write(data)


def csv_header(file):
    with open(file) as csvfile:
        return csv.reader(csvfile).next()


def csv_to_dicts(file, header=None):
    """Reads a csv and returns a List of Dicts with keys given by header row."""
    with open(file) as csvfile:
        return [row for row in csv.DictReader(csvfile, fieldnames=header)]


def edgelist_to_gml(edges, outfile):
    raw = list(map(lambda x: [x['source'], x['target'], int(x['weight'])], edges))
    ig = IGraph.TupleList(raw, weights=True, directed=True, vertex_name_attr='label')
    ig.write_gml(outfile)
