import flask
from flask import request
app = flask.Flask(__name__)

from flask_cors import CORS
CORS(app)

@app.route('/')
def default():
    return '<h1> API Server is working </h1>'

app.run()