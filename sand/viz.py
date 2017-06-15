import numpy as np

from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource


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


def _weights(v, e):
    N = len(v)
    weights = np.zeros((N, N))
    for link in e:
        weights[link['source'], link['target']] = link['value']
        weights[link['target'], link['source']] = link['value']
    return weights


def _column_data_source(nodes, weights):
    colormap = ["#444444", "#a6cee3", "#1f78b4", "#b2df8a", "#33a02c", "#fb9a99",
                "#e31a1c", "#fdbf6f", "#ff7f00", "#cab2d6", "#6a3d9a"]
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

            c = 'lightgrey' if (node1['group'] != node2['group']) else colormap[node1['group']]
            data['colors'].append(c)

    return ColumnDataSource(data)


def _add_hover(p):
    p.select_one(HoverTool).tooltips = [
        ('names', '@yname, @xname'),
        ('count', '@count'),
    ]
    return p


def matrix(data, title, size):
    weights = _weights(data['nodes'], data['links'])
    source = _column_data_source(data['nodes'], weights)
    return _add_hover(_plot(data['nodes'], source, title, size))
