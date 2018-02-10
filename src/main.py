import json
import os.path
from flask import Flask


app = Flask(__name__)

filepath = os.path.join(os.path.dirname(__file__), 'data.json')


def create_handler(endpoint):
	path = endpoint['_self']['href']
	method = endpoint['_self']['method']

	@app.route(path, methods=[method], endpoint=path)
	def handler():
		return json.dumps(data)
	return handler

with open(filepath) as json_data:
	data = json.load(json_data)
	[create_handler(x) for x in data]

@app.route('/ping')
def index():
	return 'Pong'
