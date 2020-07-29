# Write a program that calculates and displays a person’s body mass index (BMI).
# The BMI is often used to determine whether a person is overweight or
# underweight for his or her height. A person’s BMI is calculated with the
# following formula:
#                     BMI = weight  703 / height^2
# where weight is measured in pounds and height is measured in inches.

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
# The function will display the users BMI, formated to 2 decimal places
# Nothing will be returned
def display_info(BMI):
    print("BMI: ", format(BMI, ',.2f'))

# Define Main
def main():

    weight = get_weight_in_pounds()

    height = get_height_in_inches()

    BMI = calculate_BMI(height, weight)

    display_info(BMI)

# Call Main
main()
