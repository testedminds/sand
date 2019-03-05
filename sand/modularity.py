from collections import Counter


def group_index(g, membership):
    # NB: The membership vector from igraph is in the same order as labels.
    return {l: m for l, m in zip(g.vs['label'], membership)}


def number_of_outside_interactions(g, membership):
    groups = group_index(g, membership)
    edgelist_ids = [[e.source, e.target] for e in g.es]
    edges = [g.vs[ids]['label'] for ids in edgelist_ids]
    interactions = [[groups[s], groups[t]] for s, t in edges]
    return len(list(filter(lambda edge: edge[0] != edge[1], interactions)))


def cluster_score(membership):
    return sum([i * i for i in Counter(membership).values()])


def objective(g, membership, alpha=1, beta=10):
    # alpha represents a tax on the number of clusters
    # beta represents a tax on the number of interactions outside of clusters

    return alpha * cluster_score(membership) + beta * number_of_outside_interactions(g, membership)
