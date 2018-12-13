import os
import json
from flask import Flask, redirect, render_template, request, url_for
import random
from random import randint, choice, shuffle

app = Flask(__name__)

question_list = []
with open("data/questions.json", "r") as question:
    riddles = json.load(question)
    
@app.route('/', methods=["POST", "GET"])
def index():
    qw = riddles
    number = random.shuffle(riddles)
    #question1 = qw.pop(), question1 = question1
    return render_template("index.html", page_title="Home",qw=qw, number=number)
    
@app.route('/rules')
def rules():
    return render_template("rules.html", page_title="Rules")
    
@app.route('/history')
def history():
    return render_template("history.html", page_title="History")
    
@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html", page_title="Leaderboard")
     
app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)


 

   