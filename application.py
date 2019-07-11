from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    progress = 5
    return render_template('index.html', progress=progress)
