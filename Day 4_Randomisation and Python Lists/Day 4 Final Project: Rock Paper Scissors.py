import random


rock = r'''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
'''

paper = r''' _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|   
'''


scissors = r'''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
'''

game_images = [rock, paper, scissors]

print("Welcome to the ROCK SCISSOR PAPER Games!")

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors?\n "))
print("You chose:")
print(game_images[player_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if player_choice == 0:
    if computer_choice == 1:
        print("You lose!")
    elif computer_choice == 0:
        print("Tie game! Try again!")
    else:
        print("You win!")

if player_choice == 1:
    if computer_choice == 1:
        print("Tie game! Try again!")
    elif computer_choice == 0:
        print("You win!")
    else:
        print("You lose!")

if player_choice == 2:
    if computer_choice == 1:
        print("You win!")
    elif computer_choice == 0:
        print("You lose!")
    else:
        print("Tie game! Try again!")
if player_choice < 0 or player_choice >= 3:
    print("You typed wrong input!")






