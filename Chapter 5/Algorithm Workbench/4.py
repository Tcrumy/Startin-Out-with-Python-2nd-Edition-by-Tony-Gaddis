# Write a loop that asks the user to enter a number. The loop should iterate 10
# times and keep a running total of the numbers entered.

# Define a sum variable
sum = 0

# Write for loop to itereate 10 times
# promting the user to enter a number
# and adding that number to sum
for increment in range(10):

    # Prompt user for number
    num = int(input("Enter a number: "))

    # Add number to sum to keep a running total
    sum += num
