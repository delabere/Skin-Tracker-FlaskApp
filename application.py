from flask import Flask, render_template
import os
import random


app = Flask(__name__)


# creates a list of hands from image filenames
os.chdir(r'/Users/jackrickards/Documents/coding/python/CS50W/skin_tracker_app/static/images/')
hands = [file for file in os.listdir() if 'jpg' in file]


@app.route('/', methods=['GET', 'POST'])
def index():
    progress = 47
    session_hands = random.sample(hands, 2)
    return render_template('index.html', progress=progress, session_hands=session_hands)


@app.route('/data')
def data():
    return render_template()


@app.route('/logout')
def logout():
    return render_template()
