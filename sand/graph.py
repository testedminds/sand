from igraph import Graph as IGraph


def _update(s, data):
    s.update([data['source'], data['target']])
    return s


def edgelist_to_nodes(edgelist):
    return reduce(lambda acc, data: _update(acc, data), edgelist, set())


def edgelist_to_igraph(edgelist):
    raw = map(lambda x: [x['source'], x['target'], int(x['weight'])], edgelist)
    return IGraph.TupleList(raw, weights=True, directed=True, vertex_name_attr='label')
