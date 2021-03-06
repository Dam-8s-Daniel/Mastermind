"""
mastermindClass.py contains the logic on running the mastermind game using the Class Mastermind.
"""

import requests
import random
import copy


class Mastermind:

    def __init__(self):
        self.max_attempts = 10
        self.lower_limit = 0  # lowest number that a digit can be
        self.upper_limit = 7  # highest number that a digit can be
        self.max_digits = 4
        self.guesses = []  # list of player guesses each round
        self.responses = []  # list of responses to player guesses each round
        self.status = 2  # 0 = loser || 1 = winner || 2 = game ongoing
        self.wins = 0
        self.losses = 0
        self.games_played = 1
        self.current_answer = []
        self.guess_distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.guessing_allowed = True
        self.asked_for_hints = 1
        self.hint = None

    def set_lower_limit(self, new_limit: int):
        self.lower_limit = new_limit

    def set_upper_limit(self, new_limit: int):
        self.upper_limit = new_limit

    def set_max_digits(self, new_max_digit: int):
        self.max_digits = new_max_digit

    def add_guess_history(self, guess: list):
        self.guesses.append(guess)

    def add_response_history(self, guess: str):
        self.responses.append(guess)

    def is_guessing_allowed(self) -> bool:
        if len(self.guesses) < self.max_attempts:
            self.guessing_allowed = True
        else:
            self.guessing_allowed = False
        return self.guessing_allowed

    def set_current_answer(self):
        url = f"https://www.random.org/integers/?num={self.max_digits}&min={self.lower_limit}&max={self.upper_limit}&col=1&base=10&format=plain&rnd=new"
        r = requests.get(url)
        random_num_list = r.text.split()

        print("Correct Answers:" + str(random_num_list))
        random_num_list = [int(x) for x in random_num_list]
        self.current_answer = random_num_list


    def check_winner(self, correct_num_and_location: int) -> int:
        """
        Updates the game's status and, if the player wins, the number of tries that the player took.
        :param correct_num_and_location: number of correct numbers that are in the correct
        location, which is returned by check_nums
        :return: 0 = loser || 1 = winner || 2 = game ongoing
        """
        if correct_num_and_location == self.max_digits:
            self.guessing_allowed = False
            self.status = 1
            self.wins += 1
            self.guess_distribution[len(self.guesses) - 1] += 1
            return self.status
        elif len(self.guesses) == 10:
            self.guessing_allowed = False
            self.status = 0
            self.losses += 1
            return self.status
        else:
            return self.status

    def check_nums(self):
        """
        Checks the last list of numbers for correctness in the guesses list.
        Adds to the response list one of three feedback based on the correctness of the numbers.
        :return: Returns the status of the game (ongoing, loser, winner) using the check_winner method.
        """
        guess = self.guesses[-1]
        correct_number = False
        correct_num_and_location = 0

        for i in range(self.max_digits):
            if guess[i] == self.current_answer[i]:
                correct_num_and_location += 1
            elif guess[i] in self.current_answer:
                correct_number = True

        if correct_num_and_location == self.max_digits:
            self.add_response_history("Winner!")
        elif correct_num_and_location:
            self.add_response_history("You guessed one or more correct numbers that are in the right place!")
        elif correct_number:
            self.add_response_history("You guessed one or more correct numbers, but they're in the wrong place!")
        else:
            self.add_response_history("Your guess is off the mark. ALL numbers are incorrect")

        return self.check_winner(correct_num_and_location)

    def store_guess_attempt(self, numbers: list):
        """
        :param numbers: list of numbers that the user entered as a guess
        :return: None
        """
        numbers = [int(x) for x in numbers]
        self.guesses.append(numbers)

    def get_hint(self):
        """
        Allows a user to get a hint when requested.
        :return: One of three possible answers depending on how many times a hint has been asked.
        """
        # Returns the first number as a hint
        if self.asked_for_hints == 1:
            self.hint = f"The first number is {self.current_answer[0]}"

        # Returns the last number as a hint
        elif self.asked_for_hints == 2:
            self.hint = f"The last number is {self.current_answer[-1]}"

        # Return the correct numbers, but in the incorrect order
        else:
            answer_copy = copy.copy(self.current_answer)
            random.shuffle(answer_copy)
            self.hint = f"The numbers are {answer_copy}"

        self.asked_for_hints += 1

    def restart(self):
        """
        Gets new random answer and clears history of guesses and their responses.
        Updates the number of games that a player has played by 1.
        :return: None
        """
        self.set_current_answer()
        self.guesses = []
        self.responses = []
        self.guessing_allowed = True
        self.asked_for_hints = 1
        self.hint = None
        self.status = 2
        self.games_played += 1



