import json
import os.path
from flask import Flask, render_template, request

from actions import ActionHandler


app = Flask(__name__)

filepath = os.path.join(os.path.dirname(__file__), 'data.json')

action_handler = ActionHandler()

@action_handler.handler('describe')
def describe(text):
	return {'text': text}

def create_handler(endpoint):
	path = endpoint['_self']['href']
	methods = list(endpoint['_self']['methods'].keys())

	@app.route(path, methods=methods, endpoint=path)
	def handler():
		actions = endpoint['_self']['methods'][request.method]
		result = {}
		for action in actions:
			result.update(action_handler(action['action'], action.get('options', None)))
		result.update({'_links': endpoint['_links']})
		return json.dumps(result)
	return handler

with open(filepath) as json_data:
	data = json.load(json_data)
	[create_handler(x) for x in data]

@app.route('/ping')
def index():
	return 'Pong'

@app.route('/')
def client():
	return render_template('client.html')

if __name__ == '__main__':
	app.run(port=5000)
