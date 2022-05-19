# Mastermind

## Background 
Mastermind is a classic board game in which a player guesses the correct four-color sequence, determined by another player,
in 10 tries or fewer. After each round, the computer gives feedback on the correctness of the guess. The original board 
game version is played with eight different colored pegs for the sequences, and a black peg and a white peg to 
represent correctness of the colored pegs. 

There are several changes in this adaptation of the game. The first is that the eight colors are played with numbers.
The numbers of the sequence is determined by a random
number generator from random.org. You can read more on how random.org generate numbers in their 
[faq](https://www.random.org/faq/#:~:text=RANDOM.ORG%20uses%20radio%20receivers,order%20to%20affect%20the%20generator).
The second major change is that the program will give only one item of feedback, instead of up to four. 

## Game Play
The goal of the game is to guess the correct four-digit sequence. To start, 
navigate to the "play" page. The computer will generate four random numbers in the range of 0 - 7.
Two or more numbers can be the same (i.e. The sequence can be  1, 1, 1, 1).
Enter in your guess in the provided text boxes and press submit.
Any numbers will be accepted, so be careful of what you enter!
The computer will show you your guess and feedback. The feedback will come in one of three messages:
    <ol>
        <li>"You guessed one or more correct numbers that are in the right place!"</li>
        <li>"You guessed one or more correct numbers, but they're in the wrong place!"</li>
        <li>"Your guess is off the mark. ALL numbers are incorrect."</li>
    </ol>
That concludes the first round of guessing. Find the sequence in 10 rounds or fewer.
Three hints are available if needed. The first hint gives the first number. The second hint gives the last number.
The last hint gives all the numbers, but in random order. 
***
## Play the latest release
#### Online 
The latest release can be played at https://mmindgame.herokuapp.com/play (v.1.0.0, May 17, 2022).

#### Download it to your computer

Steps:
1. Download Python 3 if you don't have it already. You can download the latest version for your machine 
[here](https://www.python.org/downloads/). It is recommended to check "Add
Python to PATH" in the setup. 
2. Clone the git repository to you computer (instructions on cloning a repository can be found 
[here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)). 
Alternatively, download the files in a zip file and extract them to a directory.
3. Change the directory to where the files are stored using the terminal.
4. Create a python virtual environment by running the command 

       # mac/linux: 
       python3 -m venv venv

       # windows:
       python -m venv venv

**NB**: The last venv can be named anything you want, but for simplicity venv will be used. 
5. Activate the current environment using one of two commands:

       # mac/linux: 
       source venv/bin/activate

       # windows: 
       venv\scripts\activate.ps1
 
6. Run the following command to install requirements:
```pip install -r requirements.txt```

7. Start the game by running ```python3 app.py``` and navigate to ```localhost:5000``` on your browser
8. Deactivate the virtual environment using the command ```deactivate``` once you're done playing!

***
## Code Structure
The latest implementation of Mastermind is a Flask application, which will support the operations of the game made in Python.
The basic structure of a Flask app has two directories,
static and templates, and an entry point file called app.py.
The static directory has three directories that hold the following file types: css, img, and js.  The templates directory 
are the webpages made in jinja2. Instead of having a home page, the main entry point is the "play" page. 
This may change in the future when a login page is made.  

The logical operations of the game of Mastermind lives in mastermindClass.py. 
This file contains a definition of a class called Mastermind. A class structure was used so that extensions can be added
easily in the future.

Once instantiated, the class keeps track of the game's progress by tracking a player's history of
guesses, the responses to the guesses, the status of the game, and the current answer. The attributes to the game are 
reset for a new game. The data persisting after a new game is requested include the number of wins, the number of 
losses and the current parameters for the upper and lower ranges of numbers allowed in the game.
A player can interact with the class through endpoints as described below.

**ENDPOINTS**


```POST /submit``` - Records the numbers that a player has entered and updates the game

```GET /hint``` - Gives a player a hint based on how many times a hint has been asked

```POST /restart``` - Starts a new game. Does not reset stats

```POST /setlimits``` - Changes the range of expected numbers

## Completed extensions
1. Hints button gives three hints without penalty. The first hint gives the first number. The second hint 
gives the last number. The last hint gives all the numbers but in random order. Hints were the first extension that
was made due to the difficulty of the game.
2. The range of numbers can be adjusted in the settings menu. 
3. A "stats" page that keeps track of the number of attempts for each game that leads to a win. The stats page also 
keeps track of wins, losses, and the percent of wins. 
4. An image at the end of each game is produced depending on the outcome of the game. One image is a picture of my dog,
Luna. 

## Backlog
- [ ] Create sessions so that each player can play and record their own stats
- [ ] Login page
- [ ] Connect database to record player stats


## Backlog Description
1. The current implementation does not store sessions, and this has major implications. The first is
that any request to the server isn't tied to any other request or a particular user. This means
that there may be multiple threads of Mastermind being run on a sever, but a request to the
sever may not direct it to the correct thread, which results in unintended behavior. 
The temporary solution is to have only one process (see Procfile), which sacrifices the use of multiple
players. A more permanent solution is to store state in a session using Flask sessions. 
2. Connecting a database will allow players to store their wins, losses, and games played. The current
release stores results until the sever is reset. 
