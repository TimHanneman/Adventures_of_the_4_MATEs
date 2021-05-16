# CST 205
# Adventures of the 4 M.A.T.E.S
# This program is an interactive comic book with audio.
# By Marco-Antonio Vega, Timothy Hanneman, Anthony Rubio, and Eddie Sanchez.
# May 17, 2021
# <!-- https://github.com/TimHanneman/Adventures_of_the_4_MATEs.git -->

# Marco worked on CSTGP.py, page.html, and titlePage.html. 
# He set up routing functionality for the different pages
# and navigation bar.

# Tim worked on compiling sound assests together to work in page.html. Bug fixing in style.css, page.html, and titlePage.html
# Anthony worked on style.css, titlePage.html, bug fixing with Tim.
# Eddie worked on style.css, page.html, bug fixing with Marco.

#Each person contributed image files, and several sound files for the project to function.

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

# @app.route('/Page<pageNumber>')
# def page5(pageNumber):
#     return render_template('page5.html', pageNumber=int(pageNumber))
