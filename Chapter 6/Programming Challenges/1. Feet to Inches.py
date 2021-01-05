# One foot equals 12 inches. Write a function named feet_to_inches that accepts
# a number of feet as an argument, and returns the number of inches in that many
# feet. Use the function in a program that prompts the user to enter a number of
# feet and then displays the number of inches in that many feet.


def main():

    feet = float(input("Enter an amount in feet: "))

    inches = feet_to_inches(feet)

    print(feet, "Feet is", inches, "inches")

    
# This function will accept a float argument for feet
# It will return the amount of inches in that many feet
def feet_to_inches(feet):
    return feet * 12

main()
