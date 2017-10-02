def namespaces(labels):
    """
    Converts fully-qualified names to a list of namespaces.
    namespaces(['clojure.core/map']) => ['clojure.core']
    """
    return list(map(lambda label: label.split('/')[0], labels))


def labels_to_groups(labels):
    label_set = set(labels)
    lookup = {l: id for l, id in zip(label_set, range(len(label_set)))}
    return list(map(lambda l: lookup[l], labels))


def fqn_to_groups(labels):
    return labels_to_groups(namespaces(labels))


def edge_betweenness(g, directed=True):
    # Girvan-Newman edge betweenness-based community structure detection
    # works with directed and weighted edges and will handle multiple communities.

    # calculate dendrogram
    dendogram = g.community_edge_betweenness(directed=directed)
    # convert it into a flat clustering
    clusters = dendogram.as_clustering()
    # get the membership vector
    return clusters.membership
