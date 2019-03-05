import csv


def legal_file_name(name):
    for c in r'[]/\;,><&*:%=+@!#^()|?^':
        name = name.replace(c, ' ')
    return name.replace(' ', '_').lower()


def dictionary_list_to_csv(data, file):
    header = data[0].keys()
    with open(file, 'w') as out:
        writer = csv.DictWriter(out, header)
        writer.writeheader()
        writer.writerows(data)


def csv_header(file):
    with open(file) as csvfile:
        return csv.reader(csvfile).next()


def csv_to_dicts(file, header=None):
    """Reads a csv and returns a List of Dicts with keys given by header row."""
    with open(file) as csvfile:
        return [row for row in csv.DictReader(csvfile, fieldnames=header)]
