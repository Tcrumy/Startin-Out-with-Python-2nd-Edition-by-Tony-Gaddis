# Write code that prompts the user to enter a positive nonzero number and
# validates the input.

number = int(input("Enter a positive nonzero number: "))

# Validate the input
while number <= 0:

    print("Number was not positive/nonzero, try again")
    number = int(input("Enter a positive nonzero number: "))
