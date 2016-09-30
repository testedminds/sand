from igraph import Graph as IGraph


def edgelist_to_igraph(edgelist):
    raw = map(lambda x: [x['source'], x['target'], int(x['weight'])], edgelist)
    return IGraph.TupleList(raw, weights=True, directed=True, vertex_name_attr='label')
