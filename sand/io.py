import csv
from igraph import Graph as IGraph


def csv_to_edgelist(file, fields=['source', 'target', 'weight']):
    'Reads a csv and returns a List of Dicts with keys given by fields'
    with open(file) as csvfile:
        return [row for row in csv.DictReader(csvfile, fieldnames=fields)]


def edgelist_to_gml(edges, outfile):
    raw = map(lambda x: [x['source'], x['target'], int(x['weight'])], edges)
    ig = IGraph.TupleList(raw, weights=True, directed=True, vertex_name_attr='label')
    ig.write_gml(outfile)

