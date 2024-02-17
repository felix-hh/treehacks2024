import random
from flask import Flask, request, jsonify
from flask_cors import CORS

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

@app.route('/questions', methods=['GET'])
def get_questions():
  questions = [
    "What is the correct form of the verb 'to be' in the sentence: 'She  a doctor'?", 
    "Correct the grammatical error in this sentence: 'Me and my friend is going to the park.'", 
    "Fill in the blank with the correct form of the verb: 'If I  a millionaire, I would buy a house on the beach.'", 
    "Identify the grammatical structure of this sentence: 'The dog that is barking is mine.'", 
    "Explain the difference between 'I have eaten' and 'I was eating' in terms of grammar and context.", 
    "Correct the sentence if it's grammatically incorrect: 'She don't like apples.'", 
    "What is the past tense of the verb 'run'?", 
    "Which sentence is written in the past tense: 'I run to the store.' or 'I ran to the store.'", 
    "What is the plural form of the word 'child'?", 
    "Identify the subject and predicate in this sentence: 'The cat is sleeping on the couch.'"
    "What is the past tense of read",
    "What is the past perfect tense of run",
    "Explain the difference between 'good' and 'better'",
    "Find the mistake in the following sentence 'I dye my hair blue yesterday'"
  ]
  random.shuffle(questions)
  return jsonify(questions[:10])


@app.route('/answers', methods=['POST'])
def post_answers():
  body = request.get_json()['submission']
  print(f'Submission {body}')
  return jsonify('dabz very cool')

# @app.route('/questions', methods=['GET'])
# def get_questions():
#   question_list = ["Yay?", "Nay?"]
#   response = jsonify(question_list)
#   return response
