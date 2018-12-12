import os
import json
from flask import Flask, redirect, render_template, request 
import random
from random import randint, choice, shuffle

app = Flask(__name__)

question_list = []
with open("data/questions.json", "r") as question:
    riddles = json.load(question)
    
@app.route('/', methods=["POST", "GET"])
def home():
    qw = riddles
    number = random.shuffle(riddles)
    #question1 = qw.pop(), question1 = question1
    return render_template("index.html", page_title="Test",qw=qw, number=number)
     
app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)


 

   