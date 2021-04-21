from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from image_info import image_info
from PIL import Image
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def titlePage():
    return render_template('titlePage.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')


@app.route('/page4')
def page4():
    return render_template('page4.html')


@app.route('/page5')
def page5():
    return render_template('page5.html')


@app.route('/page6')
def page6():
    return render_template('page6.html')

@app.route('/page7')
def page7():
    return render_template('page7.html')

@app.route('/page8')
def page8():
    return render_template('page8.html')

@app.route('/page9')
def page9():
    return render_template('page9.html')

@app.route('/page10')
def page10():
    return render_template('page10.html')