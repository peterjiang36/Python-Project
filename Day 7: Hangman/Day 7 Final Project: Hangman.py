# Step 1

import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)
placeholders = ""
for count in range(1, len(chosen_word) + 1):
    placeholders += "_"

for placeholder in placeholders:
    print(placeholder, end="")
print("\n")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter which could be in the word: ").lower()
print(guess)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)



