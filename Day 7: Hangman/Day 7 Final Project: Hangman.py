# Step 1

import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholders = ""
for count in range(1, len(chosen_word) + 1):
    placeholders += "_"

for placeholder in placeholders:
    print(placeholder, end="")
print("\n")

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter which could be in the word: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"


    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")
    print(lives)



    if "_" not in display:
        game_over = True
        print("You win.")

    print(stages[lives])



