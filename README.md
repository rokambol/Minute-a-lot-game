# TEST-YOUR-KNOWLEDGE

Quiz Game test user knowledge in three round and for every correct answer user collect points 
[Test-your-knowledge](http://test-your-knowledge-quiz-game.herokuapp.com/)

## UX
 
User Stories
* As a visitor, I would like to have a look at the scoreboard to see how other players have done; it would be a good to find out how difficult the game is before I play.
* As a new player, I would like to register a username so I can play the game.
* As a player, I would like to answer some riddles, after all that's what the game is about.
* As a player, I would like to earn points for correct answers.
* As a player, I would like to be able to skip a question if I don't know the answer.
* As a player, I would like to be able to see my current score at all times.
* As a player, I would like to see where I rank on the leaderboard once I finish the game.

## Features

1. The welcome page welcomes the visitor, gives a brief story of the game and provide them with link to page with game rules and game history also user can see leaderboard 

2. The register page allows the user to register a username of their choice.Their name and  will appear in the header (see base template) 

3. User is redirect to round 1 page where they start round 1 which contains 10 different questions.A shuffled question list is prepared at this time by reading the content of the riddles file into a session-specific variable.The riddles page loads the shuffled riddle list into the jinja template where the riddle and answer are inserted: the riddle where the user can see it, the answer in a hidden form field for comparing to the answer inputted by the user, making sure the required answer matches the question. 

4. When a user answers a 10 question is redirect to round 2, where they also should answer 10 questions from various topic (score an check answer use the same methodology as round 1).

5. when 10 question are answer user is redirect to round 3 which have only 3 questions but require user to input it answer if the field, because round 3 is most difficult in the game for each correct answer user double it current score and if user answer all questions from round 3 correctly total user point double again(score an check answer use the same methodology as round 1 and 2).

6. After they finish round 3 game redirect user to lederboard page where they can see how they do compare with other users. leaderboard page can also be accessed by clicking the View Leaderboard navigation item (see base template). 

7. When the user clicks the log-out button in the nav bar, their session will be discarded and a Logged Out page will appear to confirm they logged out and to thank them for playing.

8. After round 1 question finish they are waiting period of 3 seconds before round 2 start

8. After round 2 question finish they are waiting period of 3 second before round 3 start 



### Features Left to Implement
- Due to Heroku's lack of file persistence, usernames and scores aren't currently registered in a permanent way. I would like to change this to a database in future so user details are perpetuated.
- After the previous feature is implemented, a secure sign-up and a user page with the user's personal stats (best score, dates played) would also be a nice addition. More questions would need to be added for this as well to get a broader selection for multiple replays.

## Technologies Used

As this project was build for the Practical Python Milestone Project, Python was used to create the bulk of the code: all the logic that makes this project work was written in Python.

Other technologies used in this project are:

- [Flask](http://flask.pocoo.org/), a Python Microframework
- Python Library used
    * for Flask Sessions to deal with multiple users - session;
    * for routing - flask;
    * for redirecting and rendering templates -redirect, redder_template; 
    * for login form - wtf form;
    * for implement bootstrap template - flask_bootstrap;
    * for shuffle question - random;
    * for remove used question - thread - threading;
    * for using .json files - json;
- [Jinja2](http://jinja.pocoo.org/docs/2.10/), a templating language for rendering data in the html templates, communicating between front-end and back-end.

- HTML, the most basic building block of the Web for writing the basic front-end content.

- CSS, a stylesheet language for styling the page.

- [JQuery](https://jquery.com/) for allowing the Javascript functionality in Bootstrap and my custom script to work.

- [Bootstrap](https://getbootstrap.com/), a front-end framework for general responsiveness.
for components used such as the navbar with burger icon which makes the app easy to use on mobile.


## Testing

No custom automated testing has been done on this project, but the validity of Python has been checked using Flake8, which warns for indentation issues and similar possible mistakes.

- For the user stories, the manual testing process is as follows:

- welcome page will have brief test with navbar on the top or like button on mobile version which have link to log in page where user can choose username and start the game and link to 
rules of the game and brief history page

   - As a visitor, I would like to have a look at the scoreboard to see how other players have done; it would be a good to find out how difficult the game is before I play.
    
   - In the navbar at the top of the page, click "Leaderboard". Due to Heroku's issue with file persistency, it is possible that the leaderboard doesn't show any current scores.
   
   - As a new player, I would like to register a username so I can play the game.
       - Go to the login page. You can do this from the Nav Bar, the welcome page or the leaderboard page, all of which have links inviting visitors login and play.
      - First, to check that it's a required field, try leaving the Your Username field blank. You will be asked to "Please fill out in this field".
      - Fill in a username of your choice. You will be redirected to the round 1/index page if successful.
   - In index user, you will answer 10 questions with 3 possible answer each, after all that's what the game is about. For each correct answer user receive 10 points so maximum points for round 1 are 100.
     - After 10 question answer regardless right or wrong user is start round 2 where user will answer 10 questions with 4 possible answer each. For each correct answer user receive 10 points so maximum points for round 1 are 100. If user answer correct all questions in round 1 and 2 will have 200 points.
     
  - After 10 question answer regardless right or wrong user is start round 3 where user will answer 3 questions with input field for answer. For each correct answer user double is existing points if all questions in round 3 are answer correctly game double total points. maximum points for round 1 are 100. If user answer correct all questions in round 1 and 2 will have 200 points. If user answer correct all questions in all rounds are 3200. 

  - As a player, I would like to be able to skip a question if I don't know the answer.
      - Click the 'Next' button, it will take you directly to the next question and display the in each round, or to the leaderboard if it was the last question.
  - As a player, I would like to be able to quit the game without answering all questions in case I run out of time.
      - Click the 'Log out', it will save your current score and take you directly to the leaderboard.

  - As a player, I would like to be able to see my current score at all times.
      - When a player is in session, their username and score will be displayed in the aside container.
   - As a player, I would like to see where I rank on the leaderboard once I finish the game.
    On the answer page of the last question in round 3, you will be redirects to leaderboard as well as display your score.

  - In case user is unhappy with result and want to try again after leaderboard table there is button "Try Again" Which reset user score to 0 and redirect user to round 1.
  
  - In each round in case of unactivity on the page app reload different question after 20 sec , that prevent user to check in web for right answer and prevent cheating.
  

## Deployment

As this project runs on Python, it was hosted on Heroku. Hosted platform for the project deployment is https://test-your-knowledge-quiz-game.herokuapp.com/ To be able to run the code on Heroku, a Procfile was added to tell Heroku it's a Python project (web: python app.py), as were the Config vars for IP (0.0.0.0) and PORT (5000).
The local editor for whole project [cloud9](https://c9.io)

To run the code locally:


Have fun!








## Credits
I would like to thank my fellow students for their encouragement, tips and bug reporting along the way. 

Many thanks to my mentor Guido Cecilio Garcia Bernal  for his help and tips.

### Content
-The description of the original television competiton was copied from [Wikipedia](https://en.wikipedia.org/wiki/Minuta_e_mnogo): 
The photo of background used in this site was obtained from [StockSnap](https://stocksnap.io/photo/KV6IATK4SM).




### Acknowledgements

 I received inspiration for this project from original television competition ["A minute is a lot"](http://www.minutaemnogo.tv/)
