from sand.csv import csv_to_dicts
import sand.graph as graph


def test_loading_from_edges():
    edgelist_file = './data/lein-topology-57af741.csv'
    edgelist_data = csv_to_dicts(edgelist_file, header=['source', 'target', 'weight'])
    functions = graph.from_edges(edgelist_data)
    assert len(functions.vs) == 107
