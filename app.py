"""
mastermind.py file will contain logic on routing using Flask
"""

from mastermindClass import Mastermind
from flask import Flask, request, redirect, url_for, render_template


game = Mastermind()
game.set_current_answer()

app = Flask(__name__)


@app.route('/')
def root():
    return redirect(url_for("play"))


@app.route('/play')
def play():
    """
    Displays updates to the play page to include any updates.
    submit endpoint redirects here after it makes any changes to the game.
    :return: play.jinja2
    """
    max_digits = game.max_digits
    guesses = game.guesses
    responses = game.responses
    round = len(game.guesses)
    max_attempts = game.max_attempts
    hint = game.hint
    status = game.status
    answer = game.current_answer
    return render_template("play.jinja2",
                           max_digits=max_digits,
                           guesses=guesses,
                           responses=responses,
                           round=round,
                           max_attempts=max_attempts,
                           hint=hint,
                           status=status,
                           answer=answer
                           )



@app.route('/submit', methods=["POST"])
def submit():
    """
    Updates Mastermind game with user input
    :return: redirects to play endpoint
    """
    if game.is_guessing_allowed() is False:
        return redirect(url_for("play"))
    nums = []
    for i in range(4):
        i += 1
        nums.append(request.form.get(f"{i}"))
    game.store_guess_attempt(nums)
    game.check_nums()

    return redirect(url_for("play"))

@app.route('/hint', methods=["GET"])
def hint():
    if game.asked_for_hints < 4:
        game.get_hint()
    return redirect(url_for("play"))

@app.route('/howto')
def howto():
    return render_template("howto.jinja2")


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
    return redirect(url_for("play"))


@app.route("/settings")
def settings():
    return render_template("settings.jinja2")


@app.route("/setlimits", methods=["POST"])
def set_lower_limit():
    lower_limit = request.form["lowerlimit"]
    upper_limit = request.form["upperlimit"]
    game.set_lower_limit(int(lower_limit))
    game.set_upper_limit(int(upper_limit))
    return redirect(url_for("play"))


if __name__ == "__main__":
    app.run(debug=True)




