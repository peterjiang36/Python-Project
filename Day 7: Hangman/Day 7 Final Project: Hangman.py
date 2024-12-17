import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

lives = 6

chosen_word = random.choice(word_list)

placeholders = ""
for count in range(1, len(chosen_word) + 1):
    placeholders += "_"

for placeholder in placeholders:
    print(placeholder, end="")
print("\n")

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter which could be in the word: ").lower()

    display = ""

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

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
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}. YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])



