from flask import Flask, request, jsonify
from flask_cors import CORS
import tog

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    if request.method == 'GET':
        return 'Hello, World!'
    if request.method == 'POST':
        print('testing')
        print(request.get_json())
        return 'kp kp kp'

@app.route('/initial_questions', methods=['GET'])
def get_questions():
  qs = tog.model_get_question()
  return jsonify(qs)

@app.route('/answers', methods=['POST'])
def post_answers():
  body = request.get_json()['submission']
  newqs = tog.model_post_answer(body)
  return jsonify(newqs)

