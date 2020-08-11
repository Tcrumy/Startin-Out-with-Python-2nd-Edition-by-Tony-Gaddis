# Write a while loop that lets the user enter a number. The number should be
# multiplied by 10, and the result assigned to a variable named product. The
# loop should iterate as long as product is less than 100.

# NOTE: This question is poorly worded in my opinion. The statement "Write
# a while loop that lets the user enter a number." implies that the user should
# be prompted for the number within the while loop, then the while loop should
# continue to multiply it by 10, assigning the result to the variable product.
# This is not possible. The loop control variable, product, must exist before
# the while loop otherwise an error will result.

# Prompt user for number
number_choice = int(input("Enter a number: "))

# Define your loop control variable
product = number_choice

# Multiply the entered number by 10 until
# the product is equal to or larger than 100
while product < 100:
    product *= 10
