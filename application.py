from flask import Flask
from flask_ask import Ask,question,statement,session
import random

app = Flask(__name__)
ask = Ask(app, '/')


@app.route("/hello")
def hello():
    return "Hello World!"

@ask.launch
def start_skill():
    welcome_message = 'Hello'
    return statement(welcome_message)

@ask.intent('GetNewFactIntent')
def intent():
    foo = ['Kochi is a major port city on the south-west coast of India bordering the Laccadive Sea.','It is part of the district of Ernakulam in the state of Kerala.','Kochi city is also part of the Greater Cochin region and is classified as a Tier-II city by the Government of India.','Kochi is called the Queen of the Arabian Sea','Kochi was an important spice trading centre on the west coast of India from the 14th century onwards','Kochi is known as the financial, commercial and industrial capital of Kerala']
    text = 'Hello, '+random.choice(foo)
    return statement(text)
