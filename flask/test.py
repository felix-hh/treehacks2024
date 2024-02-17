from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def echo():
    params = request.args.to_dict()
    email = params.get('emailContent')
    app.logger.info(f'Email request said: {email}')
    return jsonify(email)

