"""
mastermind.py file will contain logic on routing using Flask
"""

from mastermindClass import Mastermind
from flask import Flask, request, redirect, url_for, render_template, json


game = Mastermind()
game.set_current_answer()

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("home.jinja2")


@app.route('/howto')
def howto():
    return render_template("howto.jinja2")


@app.route('/play')
def play():
    max_digits = game.max_digits
    guesses = game.guesses
    responses = game.responses
    round = len(game.guesses)
    max_attempts = game.max_attempts
    return render_template("play.jinja2",
                           max_digits=max_digits,
                           guesses=guesses,
                           responses=responses,
                           round=round,
                           max_attempts = max_attempts
                           )


@app.route('/submit', methods=["POST"])
def submit():
    if game.check_can_guess() is False:
        return redirect(url_for("play"))
    nums = []
    for i in range(4):
        i += 1
        nums.append(request.form.get(f"{i}"))

    game.store_guess_attempt(nums)
    game.check_nums()

    return redirect(url_for("play"))

@app.route("/stats")
def display_stats():
    return render_template("stats.jinja2",
                           guess_distribution=game.guess_distribution,
                           games_played=game.games_played,
                           wins=game.wins,
                           wins_percent=round((game.wins/game.games_played) * 100, 1),
                           losses=game.losses,
                           )


@app.route("/restart", methods=["POST", "GET"])
def restart_game():
    game.restart()
    game.set_current_answer()
    return redirect(url_for("play"))


@app.route("/setlowerlimit", methods=["POST"])
def set_lower_limit():
    lower_limit = request.form["lowerlimit"]
    game.set_lower_limit(int(lower_limit))


@app.route("/setupperlimit", methods=["POST"])
def set_upper_limit():
    upper_limit = request.form["upperlimit"]
    game.set_upper_limit(int(upper_limit))


@app.route("/setmaxdigits", methods=["POST"])
def set_max_digits():
    max_digit = request.form["maxDigit"]
    game.set_max_digits(int(max_digit))


if __name__ == "__main__":
    app.run(debug=True)




