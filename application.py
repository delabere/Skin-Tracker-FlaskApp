from flask import Flask, render_template, request
import os, random


app = Flask(__name__)


# creates a list of hands from image filenames
os.chdir(r'/Users/jackrickards/Documents/coding/python/CS50W/skin_tracker_app/static/images/')
hands = [file for file in os.listdir() if 'jpg' in file]

@app.route('/', methods=['GET', 'POST'])
def index():
    session_hands = random.sample(hands, 2)
    if request.method == 'POST':
        print(
            f"The worse image was: {request.form['image_worse']} the better image was: {request.form['image_better']}")
        print(f"The new progress is: {request.form['progress']}")
        progress = int(request.form['progress'])
        return render_template('index.html', progress=progress, session_hands=session_hands)
    else:
        progress = 0
        return render_template('index.html', progress=progress, session_hands=session_hands)


@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/logout')
def logout():
    return render_template('logout.html')
