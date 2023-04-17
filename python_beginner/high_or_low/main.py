# Display art
# Generate a random account from the game data
# Format the account data into printable format.
# Ask user for a guess.
# Check if user is correct.
# Get follower count of each account.
# Use if statement to check if user is correct.
# Give user feedback on their guess.
# Making account at position B become the next account at position A

from art import logo, vs
from game_data import data
import random


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("who has more followers? type A or B").lower()

    a_follower = account_a["follower_count"]
    b_follower = account_a["follower_count"]

    is_correct = check_answer(guess, a_follower, b_follower)
    if is_correct:
        score += 1
        print(f"you are right. current score {score}")
    else:
        game_should_continue = False
        print(f"you are wrong. current score {score}")
