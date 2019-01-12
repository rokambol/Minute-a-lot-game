import os
import json
from flask import Flask, redirect, render_template, request, url_for, session, escape, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators
from wtforms.validators import InputRequired, Length
import random
import threading, time


app = Flask(__name__)
app.config['SECRET_KEY']='THISISOURSECRETKEY'
Bootstrap(app)

#class for username form
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])


#load question list for round 1
with open("data/questionRound1.json", "r") as question:
    riddles = json.load(question)
    
   
    
#load question list for round 2    
with open("data/questionRound2.json", "r") as quiz:
    quiz = json.load(quiz)
    
#load question list for round 3
with open("data/questions.json", "r") as game:
    game = json.load(game)    
 
#route for welcome.html  
@app.route('/')
def welcome():
    return render_template('welcome.html', page_title = 'welcome page')
    
#Help and supporting Functions

# Function help to have 5 sec waiting period before load next round/round2
def timer():
    done_counting = threading.Event()
    def count_to_3():
        for i in range(1, 3):
            time.sleep(1)
        done_counting.set()
    thread = threading.Thread(target=count_to_3)
    thread.start()
    done_counting.wait(3)
    return redirect(url_for('round2'))
    
# Function help to have 5 sec waiting period before load next round/round3
def timerR3():
    done_counting = threading.Event()
    def count_to_3():
        for i in range(1, 3):
            time.sleep(1)
        done_counting.set()
    thread = threading.Thread(target=count_to_3)
    thread.start()
    done_counting.wait(3)
    return redirect(url_for('round3'))
    
#route for reset score to 0 if user want to try again
@app.route('/tryAgain')
def tryAgain():
    session['score']=0
    session['count']=0
    return redirect(url_for('index'))
    
   
#popQuestion() help question not be repeat when they appear on screen
def popQuestion():
    random.shuffle(riddles)
    for item in riddles:
        return(item) 
 
#route for index.html round1

@app.route('/index', methods=["POST","GET"])
def index():
    qw = riddles
    random.shuffle(qw) #shuffle question list
    username = request.form.get('username', '')
    score = session['score']
    if request.method == 'POST':
        popQuestion()
        player_answer = request.form['player_answer']
        answer = request.form['answer']
        
#compare answer from json with user answer

        if player_answer == answer:
            session['score'] += 10
            
#limit question number to 10 in this round/ 
#after 10 click on any form button redirect page

        if player_answer == answer or player_answer != answer:
            session['count'] +=1
            if session['count'] == 10:
                timer()
                return redirect(url_for('round2'))
        
    return render_template("index.html", page_title="Round 1", 
                            qw=qw, score=score, username=username)

#route for round2.html
@app.route('/round2', methods=["POST","GET"])
def round2():
    qa = quiz
#shuffle question list
    random.shuffle(qa)
    username = request.form.get('username', '')
    score = session['score']
    if request.method == 'POST':
        player_answer = request.form['player_answer']
        answer = request.form['answer']
        
#compare answer from json with user answer

        if player_answer == answer:
            session['score'] += 10
#limit question number to 10 in this round/ 
#after 10 click on any form button redirect page
        if player_answer == answer or player_answer != answer:
            session['count'] +=1
            if session['count'] == 20:
                timerR3()
                return redirect(url_for('round3'))
    return render_template("round2.html", page_title="Round2",
                            qa=qa, score=score, username=username)
                            
#routing for round 3
    
@app.route('/round3', methods=["POST","GET"])
def round3():
    asd = game
#shuffle question list
    random.shuffle(asd)
    username = request.form.get('username', '')
    score = session['score']
    if request.method == 'POST':
        player_answer = request.form['player_answer'].lower()
        answer = request.form['answer']
#compare answer from json with user answer
        if player_answer == answer:
            session['score'] *= 2
#limit question number to 3 in this round/ 
#after 3 click on submit  on button redirect page to leaderboard
        if player_answer == answer or player_answer != answer:
            session['count'] +=1
            if session['count'] == 23:
                if session['count'] == 23 and \
                (session['score'] *2) * 3 == True:
                    session['score'] *= 2
                    return redirect(url_for('leaderboard'))
                else:
                    return redirect(url_for('leaderboard'))
                    
    return render_template("round3.html", page_title="Round3", asd=asd,
                            score=score, username=username)

    
@app.route('/rules')
def rules():
    return render_template("rules.html", page_title="Rules")
    
@app.route('/history')
def history():
    return render_template("history.html", page_title="History")

#temporary dictionary save username and score help them to be transfer to lederboard    
player_score ={} 
 
"""Displays Leaderboard Page"""    
@app.route('/leaderboard')
def leaderboard():
    if 'username' in session:
        player_score[session['username']]=session['score']
    else:
        session['username'] = 'Guest'
    return render_template("leaderboard.html", page_title="Leaderboard",
                            userScore=player_score)
                            
#route for login form when valid username is insert reset score and counter to 0

@app.route('/login', methods=['POST','GET'])
def login():
    form=LoginForm()
    if session and form.validate_on_submit():
        session['username'] = request.form['username']
        session['score'] = 0
        session['count'] = 0 #counter for click counting on answers forms
        return redirect(url_for('index'))
    return render_template("login.html",form=form, page_title="Login page")
    
#route for log user out
    
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session['count'] = 0
    return redirect(url_for('welcome'))
    
    
app.run(host=os.environ.get('IP'), port=os.environ.get('PORT'), debug=True)




