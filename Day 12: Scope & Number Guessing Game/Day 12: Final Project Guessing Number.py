from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check the user input and the actual number
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if mode == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print(logo)


def game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    # Generating a random number from 1 to 100
    random_number = randint(1, 100)
    print(random_number)

    # Set difficulties
    turns = set_difficulty()

    player_guess_number = 0
    while player_guess_number != random_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Take input from the player and make sure the input is an integer
        player_guess_number = int(input("Make a guess: "))
        turns = check_answer(player_guess_number, random_number, turns)
        if turns == 0:
            print("You've run out of guesses, you loose.")
            return
        elif player_guess_number != random_number:
            print("Guess again.")


game()
