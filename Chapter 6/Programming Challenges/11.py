# Write a program that generates a random number in the range of 1 through 100
# and asks the user to guess what the number is. If the user’s guess is higher
# than the random number, the program should display “Too high, try again.” If
# the user’s guess is lower than the random number, the program should display
# “Too low, try again.” If the user guesses the number, the application should
# congratulate the user and then generate a new random number so the game can
# start over.

# Optional Enhancement: Enhance the game so it keeps count of the number of
# guesses that the user makes. When the user correctly guesses the random number
# , the program should display the number of guesses.

import random

def main():

    # Generate a random number
    random_number = random.randint(1,101)
    
    # Prompt user for guess
    user_guess = int(input("Enter a number from 1 - 100: "))

    # Create a variable for number of guesses taken, 1 so far
    guesses = 1

    # Continue prompting the user until they get the correct answer
    while user_guess != random_number:

        # Use an if else structure to give hints
        if user_guess > random_number:
            user_guess = int(input("Too high, try again: "))

        else:
            user_guess = int(input("Too low, try again: "))

        guesses += 1

    print("You have guessed correctly!")
    print("Number of guesses: ", guesses)

main()
    
