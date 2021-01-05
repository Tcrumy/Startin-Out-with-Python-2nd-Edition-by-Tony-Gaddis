# Write a program that lets the user play the game of Rock, Paper, Scissors
# against the computer. The program should work as follows.
# 1. When the program begins, a random number in the range of 1 through 3 is
# generated. If the number is 1, then the computer has chosen rock. If the
# number is 2, then the computer has chosen paper. If the number is 3, then the
# computer has chosen scissors. (Don’t display the computer’s choice yet.)
#
# 2. The user enters his or her choice of “rock”, “paper”, or “scissors” at the
# keyboard.
#
# 3. The computer’s choice is displayed.
# 
# 4. A winner is selected according to the following rules:
# • If one player chooses rock and the other player chooses scissors, then rock
# wins. (The rock smashes the scissors.)
# • If one player chooses scissors and the other player chooses paper, then
# scissors wins. (Scissors cuts paper.)
# • If one player chooses paper and the other player chooses rock, then paper
# wins. (Paper wraps rock.)
# • If both players make the same choice, the game must be played again to
# determine the winner.

import random

def main():

    # Display title
    print("Rock, paper, sissors game!")

    # Genreate the computers choice
    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        cpu_choice = "rock"
    elif comp_choice == 2:
        cpu_choice = "paper"
    else:
        cpu_choice = "sissors"
        

    # Prompt use for thier choice
    user_choice = input("Enter rock, paper, or sissors: ")

    # Display choices
    print("Player choice: ", user_choice.lower())
    print("CPU Choice:    ", cpu_choice)
    
    # Determine the winner
    if comp_choice == 1 and user_choice.lower() == "paper":
        print("Paper covers rock, Player wins!")
    elif comp_choice == 1 and user_choice.lower() == "sissors":
        print("Rock crushes sissors, Computer wins!")
    elif comp_choice == 2 and user_choice.lower() == "rock":
        print("Paper covers rock, Computer wins!")
    elif comp_choice == 2 and user_choice.lower() == "sissors":
        print("Sissors cut paper, Player wins!")
    elif comp_choice == 3 and user_choice.lower() == "paper":
        print("Sissors cut paper, Computer wins!")
    elif comp_choice == 3 and user_choice.lower() == "rock":
        print("Rock crushes sissors, Player wins!")
    # The game was a draw in this case
    else:
        print("This game is a draw")

main()
    
