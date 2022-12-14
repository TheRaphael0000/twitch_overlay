import json

from flask import Flask
from flask import render_template

config = json.load(open("config.json", "r"))

app = Flask(__name__)


@app.route("/chat")
def chat():
    return render_template('chat.html', config=config)


@app.route("/events")
def events():
    return render_template('events.html', config=config)


@app.route("/time")
def time():
    return render_template('time.html', config=config)


@app.route("/join")
def join():
    return render_template('join.html', config=config)
