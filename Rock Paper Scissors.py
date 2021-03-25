# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
#
# Remember the rules:
#
# Scissors cuts paper.
# Paper covers rock.
# Rock crushes lizard.
# Lizard poisons Spock.
# Spock smashes scissors.
# Scissors decapitates lizard.
# Lizard eats paper.
# Paper disproves Spock.
# Spock vaporizes rock.
# Rock crushes scissors.
from random import choice
import null as null

options_of_weapons = ["rock", "paper", "scissors", "lizard", "spock"]

## validiation of input
def validity(input):
    if input in options_of_weapons:
        return True
    else:
        print("Invalid input, please choose from the following: \n Rock \n Paper \n Scissors \n Spock \n Lizard ")
        return False

#Rules set out to show winning ouput against loser input
rules = {"scissors": ['paper', 'lizard'],
         'paper': ['rock', 'spock'],
         'rock': ['scissors', 'lizard'],
         'spock': ['scissors', 'rock'],
         'lizard': ['spock', 'paper']}

## defines the strcutre of the game play in accordance to rules above
def game_play(f_input, s_input):
    # if str(f_input) == str(s_input):
    #     return f_input and s_input
    if s_input in rules[f_input]:
        return f_input
    elif f_input in rules[s_input]:
        return s_input
    else:
        return null

## defines the result from game play above
def game_result(first_player, second_player):
    result = game_play(first_player, second_player)

    if result == first_player:
        print(f"First player wins, {first_player} beats {second_player}  " "🎉🎊"" ")
    if result == second_player:
        print(f"Second player wins, {second_player} beats {first_player}  " "🎉🎊"" ")
    if result == null:
        print("You drew the same one, 🤝")

## defines the contunition of the game

def user_play_again():
    do_you_want_to_play = True
    while do_you_want_to_play:
        play_again = input("Would you like to play again? Y or N? ").upper()
        if play_again == 'Y':
            return True
        elif play_again == 'N':
            return False
        else:
            print("Choose either Y or N")  ### Why does it always bounce on this, if i didnt add the user input??



## Main game executions
print("Welcome to the rock paper scissors game (Two player version)")
player_is_playing = True

while player_is_playing:
    play_who = input("Do you want to play the computer or person?").lower()
    if play_who == "computer":
        first_player_input = input("Player 1, what do you choose?").lower()
        if validity(first_player_input):
            comp = choice(options_of_weapons)
            print(comp)
            game_result(first_player_input,comp)
        else:
            player_is_playing = False
    elif play_who == "person":
        first_player_input = input("Player 1, what do you choose?").lower()
        second_player_input = input("Player 2, what do you choose?").lower()
        if validity(first_player_input) and validity(second_player_input):
            game_result(first_player_input, second_player_input)
    else:
        print(" please choose between person and computer")
    player_is_playing = user_play_again()

#
# test_game_play()
# Dictionaries and how they work
# Function for the outcome
# Divide into functions
# Computer v human OR human v human
# Encryptions??