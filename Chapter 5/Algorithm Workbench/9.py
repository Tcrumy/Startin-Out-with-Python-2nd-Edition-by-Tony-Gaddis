# Write code that prompts the user to enter a number in the range of 1 through
# 100 and validates the input.

number = int(input("Enter a number 1-100: "))

# Validate the input
while number < 1 or number > 100:

    print("Number was not in range 1-100, try again")
    number = int(input("Enter a number 1-100: "))

