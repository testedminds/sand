import csv


def __positions_to_csv(positions, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(positions)


def positions_to_csv(network, path):
    view = network.get_first_view()
    __positions_to_csv(view_to_positions(view), path)


def view_to_positions(view):
    return [[n['data']['label'], n['position']['x'], n['position']['y']]
            for n in view['elements']['nodes']]


def positions_from_csv(path):
    # Read in positions from CSV in the form ['label', 'x', 'y'] to a dict of {label [x, y]}
    with open(path, mode='r') as infile:
        reader = csv.reader(infile)
        positions = dict((rows[0], [rows[1], rows[2]]) for rows in reader)
    return positions


def __previous_positions(labels, positions, node_ids):
    previous_positions = []

    for label in labels:
        if label in positions:
            position = positions[label]
            previous_positions.append([node_ids[label], position[0], position[1]])
    return previous_positions


def __update_layout(network, previous_positions, client):
    response = client.layout.apply_from_presets(network, positions=previous_positions)
    if response.status_code != 200:
        raise RuntimeError('Presets could not be saved successfully...')


def layout_from_positions_csv(network, path, client):
    view = network.get_first_view()

    # Create a lookup table of suid's: {label suid}
    node_ids = {n['data']['label']: n['data']['SUID'] for n in view['elements']['nodes']}

    labels = [n['data']['label'] for n in view['elements']['nodes']]
    positions = positions_from_csv(path)
    previous_positions = __previous_positions(labels, positions, node_ids)
    __update_layout(network, previous_positions, client)
