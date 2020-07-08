# Write a program that asks the user to enter a distance in kilometers, and then
# converts that distance to miles. The conversion formula is as follows:
# Miles = Kilometers * 0.6214

# NOTE: This question doesn't say to write this as a function, but since chapter
# 3 is about writing functions, that is how we will write the program. Every
# program should have a main function which controls the overall program. This
# allows a high level of organization of the programs functionality, and
# centralized the commands given to the program


# The main function will prompt the user to enter kilometers to convert to miles
# and pass that argument to the kilometers_to_convert function inside the print
# function displaying the converted number to the user
def main():

    kilometers_to_convert = float(input("Enter kilometers to convert to miles: "))

    print(kilometers_to_miles(kilometers_to_convert))

# The kilometers_to_miles function will accept a float argument for kilometers
# convert the argument to miles and return the converted number to the calling
# function
def kilometers_to_miles(kilometers):
    multiplier = 0.6214
    miles = kilometers * multiplier

    # This return statement shows that this function is a value returning function
    return miles

main()
