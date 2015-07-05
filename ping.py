#!flask/bin/python
import os
from flask import Flask
from time import sleep

port = int(os.environ.get('PORT', 8000))
app = Flask(__name__)

@app.route('/')
def index():
    """Index Redirect Page"""
    return '''yo'''


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)
