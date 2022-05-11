"""
mastermindClass.py contains the logic on running the mastermind game.
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
        self.guesses = []
        self.response = []
        self.wins = 0
        self.losses = 0
        self.current_answer = []
        self.guessing_allowed = True

    def set_lower_limit(self, new_limit: int):
        self.lower_limit = new_limit

    def set_upper_limit(self, new_limit: int):
        self.upper_limit = new_limit

    def set_max_digits(self, new_max_digit: int):
        self.max_digits = new_max_digit

    def add_guess_history(self, guess: list):
        self.guesses.append(guess)

    def add_response_history(self, guess: str):
        self.response.append(guess)

    def check_can_guess(self) -> bool:
        if len(self.guesses) < self.max_attempts:
            self.guessing_allowed = True
        else:
            self.guessing_allowed = False
        return self.guessing_allowed

    def set_random_nums(self):
        url = f"https://www.random.org/integers/?num={self.max_digits}&min={self.lower_limit}&max={self.upper_limit}&col=1&base=10&format=plain&rnd=new"
        r = requests.get(url)
        random_num_list = r.text.split()
        print("Correct Answers:" + str(random_num_list))
        self.current_answer = random_num_list

    def check_nums(self, guess: list):
        correct_number = False
        correct_num_and_location = 0

        for i in range(self.max_digits):
            if guess[i] == self.current_answer[i]:
                correct_num_and_location += 1
            elif guess[i] in self.current_answer:
                correct_number = True

        if correct_num_and_location:
            self.add_response_history("You guessed one or more correct numbers and they're in the right place!")
        elif correct_number:
            self.add_response_history("You guessed one or more correct numbers, but they're in the wrong place!")
        else:
            self.add_response_history("Your guess is off the mark. ALL numbers are incorrect")

        return correct_num_and_location

    def check_winner(self, correct_num_and_location: int) -> int:
        if correct_num_and_location == self.max_digits:
            self.guessing_allowed = False
            self.wins += 1
            return 1
        elif len(self.guesses) == 10:
            self.guessing_allowed = False
            self.losses += 1
            return 0
        else:
            return 2

    def get_guess_attempt(self):
        if self.check_can_guess():
            return "Can't guess anymore!"
        guess = []
        i = 0
        while i < self.max_digits:
            print(f"Enter a number for slot # {i+1}:")
            val = input()
            int_val = int(val)
            if i < self.lower_limit or i > self.upper_limit:
                print(f"Enter a number between {self.lower_limit} and {self.upper_limit}")
            else:
                guess.append(val)
                i += 1

    def get_hint(self, num: int):

        if num == 1:
            return self.current_answer[0]

        elif num == 2:
            return self.current_answer[-1]

        #Return the numbers, but in the incorrect order
        else:
            answer_copy = copy.copy(self.current_answer)
            random.shuffle(answer_copy)
            return answer_copy


    def restart(self):
        self.set_random_nums()
        self.lower_limit = 0
        self.upper_limit = 7
        self.max_digits = 4
        self.guesses = []
        self.response = []
        self.current_answer = []
        self.guessing_allowed = True



