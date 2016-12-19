import requests
import json

# Basic Setup
PORT_NUMBER = 1234
BASE = 'http://localhost:' + str(PORT_NUMBER) + '/v1/'

# Header for posting data to the server as JSON
HEADERS = {'Content-Type': 'application/json'}

VERSION_URL = BASE + 'version'


def print_version():
    response = requests.get(VERSION_URL)
    print(json.dumps(response.json(), indent=2))

