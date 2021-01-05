# In programming Exercise #6 in Chapter 3 you were asked to write a program
# that calculates a person’s body mass index (BMI). Recall from that exercise
# that the BMI is often used to determine whether a person is overweight or
# underweight for their height. A person’s BMI is calculated with the formula:
#                    BMI = weight  703 / height^2
# where weight is measured in pounds and height is measured in inches. Enhance
# the program so it displays a message indicating whether the person has optimal
# weight, is underweight, or is overweight. A person’s weight is considered to
# be optimal if his or her BMI is between 18.5 and 25. If the BMI is less than
# 18.5, the person is considered to be underweight. If the BMI value is greater
# than 25, the person is considered to be overweight.

# NOTE: Since this is an enhancement of program 6 from chapter 3
# We will mostly use that program, but add a function to do the
# BMI check and display the message

# This function accepts no arguments
# The user will be prompted for their wieght in pounds
# The value will be returned as a float
def get_weight_in_pounds():
    weight = float(input("Enter weight in pounds: "))
    return weight

# This function will accept no arguments
# The user will be prompted to enter their height in inches
# The value will be returned as a float
def get_height_in_inches():
    height = float(input("Enter height in inches: "))
    return height

# This function will accept two float arguments height and weight
# The arguments will be used to calculate the users BMI
# The users BMI will be returned as a float
def calculate_BMI(height, weight):

    # We will return the results of the BMI formula using the arguments provided
    return (weight * 703 / (height**2))

# This function will accept one float argument
# The function will check the users BMI, and display
# a message letting them know what range they fall in
# Nothing will be returned
def display_info(BMI):

    print("Your BMI is", format(BMI, ",.2f"))
    
    if BMI > 26:
        print("You are overweight")
    elif BMI >= 18.5 and BMI <= 25:
        print("Your weight is ideal")
    else:
        print("You are underwight")

# Define Main
def main():

    weight = get_weight_in_pounds()

    height = get_height_in_inches()

    BMI = calculate_BMI(height, weight)

    display_info(BMI)

# Call Main
main()
