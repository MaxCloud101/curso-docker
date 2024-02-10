from flask import Flask, request
from flask import json
from utils import welcome_message

app = Flask(__name__)

@app.route("/")
def hello_world():
    return welcome_message()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)