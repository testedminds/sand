from igraph import Graph as IGraph


def edgelist_to_nodes(edgelist):
    return reduce(lambda acc, data: acc.union([data['source'], data['target']]), edgelist, set())


def edgelist_to_igraph(edgelist):
    raw = map(lambda x: [x['source'], x['target'], int(x['weight'])], edgelist)
    return IGraph.TupleList(raw, weights=True, directed=True, vertex_name_attr='label')
