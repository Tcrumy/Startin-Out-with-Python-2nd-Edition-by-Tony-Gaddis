# Write a loop that calculates the total of the following series of numbers:
#  1/30 + 2/29 + 3/28 +....30/1

# The easiest way to do this is to define a numerator and denominator
# variable and, with each loop, increment the numerator and decrement
# the denominator
numerator = 1
denominator = 30

# Define a variable for running total
total = 0

# Write for loop to add the given series above
for loop in range(30):

    total += numerator/denominator

    numerator += 1
    denominator -= 1
