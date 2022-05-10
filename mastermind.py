"""
Mastermind

The goal is to guess the sequence of four numbers that are randomly selected from numbers 0 - 7. Duplicates numbers are
possible.You have 10 tries. Every round consists of guessing four numbers. After each round, you'll receive slightly
helpful feedback on the correctness of the numbers. The feedback message will not say which numbers are correct.

The feedback will be one of the three messages:

1. "One or more numbers are correct and are in the correct location"
2. "One or more numbers are correct"
3. "All numbers are incorrect"

"""

import requests
import json

LOWERLIMIT = 0
UPPERLIMIT = 7
MAXDIGITS = 4

"""
GetNums
No params
return: list of random numbers as strings
"""
def GetNums():
    url = f"https://www.random.org/integers/?num={MAXDIGITS}&min={LOWERLIMIT}&max={UPPERLIMIT}&col=1&base=10&format=plain&rnd=new"
    r = requests.get(url)
    randomNumList = r.text.split()
    print("Correct Answers:" + str(randomNumList))
    return randomNumList

def main():
    numOfGuesses = 0
    while numOfGuesses < 10:

        if numOfGuesses == 0:
            randomNumList = GetNums()

        guesses = []
        print(f"You are on round {numOfGuesses + 1} of 10 guesses")

        i = 0
        while i < 4:
            print(f"Enter a number for slot # {i + 1}: ")
            val = input()
            int_val = int(val)
            if i < LOWERLIMIT or i > UPPERLIMIT:
                print("Enter a number between 0 and 7")
                continue
            guesses.append(val)
            i += 1

        numOfGuesses += 1


        print(f"Your guess: {guesses}")

        correctNumber = False
        correctNumberLocation = False

        numOfCorrectNumberLocation = 0

        #check for correctness
        for i in range(MAXDIGITS):
            if guesses[i] == randomNumList[i]:
                correctNumberLocation = True
                numOfCorrectNumberLocation += 1
            elif guesses[i] in randomNumList:
                correctNumber = True

        if numOfCorrectNumberLocation == MAXDIGITS:
            print("Winner!")
            print("Would you like to restart? (y/n)")
            yn = input()
            yn = yn.lower()
            if yn == "y" or yn == "yes":
                numOfGuesses = 0
                continue
            else:
                break

        if correctNumberLocation:
            print("One or more numbers are correct and are in the correct location\n")
        elif correctNumber:
            print("One or more numbers are correct\n")
        else:
            print("All numbers are incorrect\n")


if __name__ == "__main__":
    main()




