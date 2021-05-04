from flask import Flask, render_template
from flask_bootstrap import flask_bootstrap


app = Flask(__name__)
# bootstrap = Bootstrap(app)

@app.route('/')
def hello():
    return 'Hello world from FLask!'

