# Step 1
import random


# import hangman_words
from hangman_words import word_list

word_chosen = random.choice(word_list)
# word_chosen = random.choice(hangman_words.word_list)


#  TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#  TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#  TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
lives = 6
word_chosen = random.choice(word_list)
print(f"psst the solution is {word_chosen}")

display = []

for letter in range(len(word_chosen)):
    display += "_"


guess = ""

end_of_game = False

from hangman_art import logo

print(logo)

while not end_of_game:
    guess = input("Gues a letter.\n").lower()

    if guess in display:
        print(f"You already guesssed, {guess}")

    for position in range(len(word_chosen)):
        letter = word_chosen[position]
        if guess == letter:
            display[position] = letter

    if guess not in word_chosen:

        print(f"You guessed {guess}, that's not in the word, you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    from hangman_art import stages

    print(stages[lives])
