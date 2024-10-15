# Step 1

import random

word_list = ["aardvark", "baboon", "camel"]

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
    print(guess)

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

    if "_" not in display:
        game_over = True
        print("You win.")


