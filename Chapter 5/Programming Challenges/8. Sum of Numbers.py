# Write a program with a loop that asks the user to enter a series of positive
# numbers. The user should enter a negative number to signal the end of the
# series. After all the positive numbers have been entered, the program should
# display their sum.

# Define a sentinel variable
number = 0

print("To stop the program, enter a negative number")

# Define an acculator variable
total = 0

while number >= 0:

    total += number
    number = int(input("Enter a number to add to the sum: "))
    

print("Sum: ", total)
