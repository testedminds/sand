import numpy as np

from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource

from .graph import (vertices_to_dicts, edges_to_dicts)


def matrix(graph, sort_by, title, size, palette):
    vertices = vertices_to_dicts(graph)
    edges = edges_to_dicts(graph)
    weights = _weights(vertices, edges, graph.is_directed())
    sorted_labels = [v['label'] for v in sorted(vertices, key=lambda x: x.get(sort_by, 'group'))]
    source = _column_data_source(vertices, weights, palette)
    p = _plot(vertices, sorted_labels, sort_by, source, title, size)
    return _add_hover(p)


def _weights(v, edges, directed):
    N = len(v)
    weights = np.zeros((N, N))

    for e in edges:
        weights[e['target'], e['source']] = e['weight']
        if not directed:
            weights[e['source'], e['target']] = e['weight']
    return weights


def _column_data_source(nodes, weights, palette):
    data = dict(
        xname=[],
        yname=[],
        colors=[],
        alphas=[],
        weight=weights.flatten())

    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes):
            data['xname'].append(node1['label'])
            data['yname'].append(node2['label'])

            if (node1['group'] == node2['group']) and (weights[i, j] > 0):  # ingroup relationship
                group_color = palette[node1['group']]
                alpha = 1.0
            elif (node1['label'] == node2['label']):  # diagonal
                group_color = 'lightgrey'
                alpha = 0.2
            elif (weights[i, j] > 0):  # outgroup relationship
                group_color = 'grey'
                alpha = 0.9
            else:  # no relationship
                group_color = 'lightgrey'
                alpha = 0.1

            data['alphas'].append(alpha)
            data['colors'].append(group_color)

    return ColumnDataSource(data)


def _plot(vertices, sorted_labels, sort_by, source, title, size):
    p = figure(title=title,
               x_axis_location="above",
               tools="hover,save",
               x_range=list(reversed(sorted_labels)),
               y_range=sorted_labels,
               name=sort_by)

    p.plot_width = size
    p.plot_height = size
    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "6pt"
    p.axis.major_label_standoff = 0
    p.xaxis.major_label_orientation = np.pi / 3

    # http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.figure.Figure.rect
    p.rect('xname',
           'yname',
           0.9,
           0.9,
           source=source,
           color='colors',
           alpha='alphas',
           line_color=None,
           hover_line_color='black',
           hover_color='colors')

    return p


def _add_hover(p):
    p.select_one(HoverTool).tooltips = [
        ('names', '@yname, @xname'),
        ('weight', '@weight'),
    ]
    return p
