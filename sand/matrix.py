from IPython.display import IFrame
from string import Template
import json
import uuid
import graph


def _to_d3_nodes(edge_list):
    nodes = graph.edgelist_to_nodes(edge_list)
    return map(lambda x, y: {'id': x, 'name': y, 'group': 1}, range(len(nodes)), nodes)


def _to_d3_edges(nodes, edge_list):
    # Turn these into a lookup table to find node ids by name when creating the edges
    node_index = dict((x['name'], x['id']) for x in nodes)
    return map(lambda x: {'source': node_index[x['source']], 'target': node_index[x['target']], 'value': int(x['weight'])}, edge_list)


# Given this edge list:
# ```
# [{'source': 'node3', 'target': 'node2','weight': '1'},
#  {'source': 'node1', 'target': 'node3','weight': '3'}]
# ```
#
# ...produce json in D3 format:
# ```
# {
#       "nodes":[
#                 {"name":"node1","group":1},
#                 {"name":"node2","group":2},
#                 {"name":"node3","group":2},
#                 {"name":"node4","group":3}],
#       "links":[
#                 {"source":2,"target":1,"weight":1},
#                 {"source":0,"target":2,"weight":3}]
#     }
#       ]
# }
def _to_json(edge_list, uid):
    nodes = _to_d3_nodes(edge_list)
    edges = _to_d3_edges(nodes, edge_list)
    d3_json = json.dumps({'nodes': nodes, 'links': edges})

    json_filename = 'network-{}.json'.format(uid)
    json_file = './figure/{}'.format(json_filename)
    target = open(json_file, 'w')
    target.write(d3_json)
    target.close()
    return json_filename


def _template():
    with open('templates/matrix.html', 'r') as data:
        return Template(data.read())


def matrix(edge_list, height=400):
    uid = str(uuid.uuid4())
    json_file = _to_json(edge_list, uid)
    filename = "graph-{}.html".format(uid)
    html = _template().substitute(json_file=json_file, scale=height, source=filename)

    figure = "figure/{}".format(filename)
    with open(figure, "w") as result:
        result.write(html)

    return IFrame(figure, width="100%", height=height)
