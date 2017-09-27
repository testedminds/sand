import requests
import json

# Basic Setup
PORT_NUMBER = 1234
BASE = 'http://localhost:' + str(PORT_NUMBER) + '/v1/'

# Header for posting data to the server as JSON
HEADERS = {'Content-Type': 'application/json'}


def print_version():
    response = requests.get(BASE + 'version')
    print(json.dumps(response.json(), indent=2))


def hide_panels():
    state = [{"name": "SOUTH", "state": "HIDE"},
             {"name": "EAST", "state": "HIDE"},
             {"name": "WEST", "state": "HIDE"},
             {"name": "SOUTH_WEST", "state": "HIDE"}]
    response = requests.put(BASE + 'ui/panels/', data=json.dumps(state), headers=HEADERS)
    return response.status_code == requests.codes.ok


def lock_node_width_and_height(stylename, enabled=True):
    lock = [{'visualPropertyDependency': 'nodeSizeLocked', 'enabled': enabled}]
    response = requests.put(BASE + 'styles/' + stylename + '/dependencies', data=json.dumps(lock), headers=HEADERS)
    return response.status_code == requests.codes.no_content
