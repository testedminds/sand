import numpy as np

from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource


# pass an igraph instance to this function, then render based on the igraph attr
# igraph to dict: vertices, edges,
# specify an element to sort by, since we can do
# sorted(reviews.vs, key=lambda x: x['name'])

def matrix(data, title, size, palette):
    weights = _weights(data['nodes'], data['links'])
    source = _column_data_source(data['nodes'], weights, palette)
    return _add_hover(_plot(data['nodes'], source, title, size))


def _weights(v, e):
    N = len(v)
    weights = np.zeros((N, N))
    for link in e:
        weights[link['source'], link['target']] = link['value']
        weights[link['target'], link['source']] = link['value']
    return weights


def _column_data_source(nodes, weights, palette):
    data = dict(
        xname=[],
        yname=[],
        colors=[],
        alphas=[],
        count=weights.flatten())

    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes):
            data['xname'].append(node1['name'])
            data['yname'].append(node2['name'])

            data['alphas'].append(min(weights[i, j] / 4.0, 0.9) + 0.1)

            group_color = 'lightgrey' if (node1['group'] != node2['group']) else palette[node1['group']]
            data['colors'].append(group_color)

    return ColumnDataSource(data)


def _plot(nodes, source, title, size):
    names = [node['name'] for node in sorted(nodes, key=lambda x: x['group'])]

    p = figure(title=title,
               x_axis_location="above",
               tools="hover,save",
               x_range=list(reversed(names)),
               y_range=names)

    p.plot_width = size
    p.plot_height = size
    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_text_font_size = "5pt"
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
        ('count', '@count'),
    ]
    return p
