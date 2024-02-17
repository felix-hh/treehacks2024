from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/funkp', methods=['POST'])
def hello():
  body = request.get_json()['submission']
  print(f'Submission {body}')
  return 'dabz very cool'

@app.route('/questions', methods=['GET'])
def get_questions():
  question_list = ["Yay?", "Nay?"]
  response = jsonify(question_list)
  return response

@app.route('/answer', methods=['POST'])
def post_answers():
  body = request.get_json()
  answer_list = body
  response = jsonify(answer_list)
  return response