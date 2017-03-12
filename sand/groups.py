def namespaces(labels):
    """
    Converts fully-qualified names to a list of namespaces.
    namespaces(['clojure.core/map']) => ['clojure.core']
    """
    return list(map(lambda label: label.split('/')[0], labels))


def namespaces_to_ids(namespaces):
    ns_set = set(namespaces)
    ns_lookup = {ns: id for ns, id in zip(ns_set, range(len(ns_set)))}
    return list(map(lambda ns: ns_lookup[ns], namespaces))


def labels_to_groups(labels):
    return namespaces_to_ids(namespaces(labels))
