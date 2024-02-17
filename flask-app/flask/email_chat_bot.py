from flask import Flask
from flask import request, jsonify, Response
from flask_cors import CORS

import os
import sys
import logging
from llama_index import (
    StorageContext,
    load_index_from_storage,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

root_dir = os.curdir
persist_dir = os.path.join(root_dir, 'llama_index', 'train_emails', 'storage')
key = os.environ['OPENAI_API_KEY']

from google_api.send_email import gmail_send_message

def get_index():
    # set up logging 
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
    
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    index = load_index_from_storage(storage_context)
    return index

index = get_index()
chat_engine = index.as_chat_engine(verbose=True)

@app.route('/emailgenerate', methods=['GET'])
def email_generate():
    params = request.args.to_dict()
    prompt = params.get('prompt')
    app.logger.info(f'Email request said: {prompt}')
    response = jsonify(chat_engine.chat(prompt).response)
    return response


@app.route('/emailsend', methods=['POST'])
def email_send():
    try:
        body = request.get_json()
        app.logger.info(body)
        gmail_send_message(body['email'], "splitdevran@gmail.com", body['subject'], body['message'])
        return jsonify('Sucesss')
    except BaseException as err:
        return jsonify(f'Failed to send email {err.text}')
    