from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)

href="{{ url_for('static', filename='style.css')}}"


@app.route('/')
def titlePage():
    return render_template('titlePage.html')

@app.route('/page<pageNumber>')
def page(pageNumber):
    return render_template('page.html', pageNumber=int(pageNumber))