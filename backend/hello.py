from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

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
        # gmail_send_message(body['email'], "splitdevran@gmail.com", body['subject'], body['message'])
        return jsonify('Sucesss')
    except BaseException as err:
        return jsonify(f'Failed to send email {err.text}')
    