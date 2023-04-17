# choosing a random number between 1 and 100
# make function to set difficulty
# let the user guess a number
# function to check user's guess
# track attemps, reduce
# repeat guessing functionality

import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("too high")
        return turns - 1
    elif guess < answer:
        print("too low")
        return turns - 1
    else:
        print(f"you win, answer: {answer}")


def set_difficulty():
    level = input("choose a difficulty, type easy or hard")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Find the number between 1 and 100")

    answer = random.randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attemps remaining to guess the number")
        guess = int(input("make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you have run out of guesses, you lose")
            return
        elif guess != answer:
            print("guess again")


game()
