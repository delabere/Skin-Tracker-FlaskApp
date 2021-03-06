from flask import Flask, render_template, request, Session
import os
import random
import json


app = Flask(__name__)
Session(app)

# creates a list of hands from image filenames
hands = [file for file in os.listdir(r'static/images') if 'jpg' in file]

# read in stored hand_data
with open(r'static/temp_storage/storage.json') as json_file:
    storage = json.load(json_file)


def hand_picker(storage):
    hands_data = [[file, storage[file]['position'], storage[file]['times_sorted']]
                  for file in storage]
    random.shuffle(hands_data)
    hands_data = (sorted(hands_data, key=lambda x: int(x[2])))
    first, second = hands_data.pop(), hands_data.pop()
    return [first, second]


@app.route('/', methods=['GET', 'POST'])
def index():
    session_hands = hand_picker(storage)
    print(session_hands)
    if request.method == 'POST':
        worse = request.form['worse']
        better = request.form['better']
        print(worse, better, 'sdfsf')  # todo: get rid of this
        progress = int(request.form['progress'])
        if progress >= 100:
            progress = 100
        return render_template('index.html', progress=progress,
                               session_hands=session_hands)

    else:
        progress = 0
        return render_template('index.html', progress=progress,
                               session_hands=session_hands)


@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/logout')
def logout():
    return render_template('logout.html')
