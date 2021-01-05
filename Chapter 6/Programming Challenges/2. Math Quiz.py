# Write a program that gives simple math quizzes. The program should display two
# random numbers that are to be added, such as:
#      247
#    + 129
# The program should allow the student to enter the answer. If the answer is
# correct, a message of congratulations should be displayed. If the answer is
# incorrect, a message showing the correct answer should be displayed.

# You will need the random library for this program
import random

def main():

    # Create two random numbers to use in the equation
    num1 = random.randint(0,999)
    num2 = random.randint(0,999)

    # Find the sum so you can compare the users
    # answer to the correct answer
    sum = num1 + num2

    # Display the instructions and the equation to the user
    print("Please answer the following math problem/n")
    
    print(format(num1, "5d"))
    print("+", format(num2,"3d"))
    print("-----\n")

    # Get the users answer
    answer = int(input("Enter your answer: "))

    # Determine the correct answer to display to the user
    if answer == sum:
        print("\nYou are correct")
        print(format(num1, "5d"))
        print("+", format(num2,"3d"))
        print("-----")
        print(format(sum, "5d"))

    else:
        print("\nYou are incorrect")
        print(format(num1, "5d"))
        print("+", format(num2,"3d"))
        print("-----")
        print(format(sum, "5d"))

# Call main
main()
        

    
