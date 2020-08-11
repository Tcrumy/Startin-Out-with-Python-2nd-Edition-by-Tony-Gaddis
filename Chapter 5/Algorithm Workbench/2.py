# Write a while loop that asks the user to enter two numbers. The numbers should
# be added and the sum displayed. The loop should ask the user if he or she
# wishes to perform the operation again. If so, the loop should repeat,
# otherwise it should terminate.

# Define the loop control variable
repeat_operation = "y"

# Write a while loop that prompts user for two numbers
# then sums and displays the numbers for as long as the
# user wants to repeat the operation
while repeat_operation == "y":

    # Prompt user for numbers
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    sum = num1 + num2
    
    print("Sum:", sum)

    # Ask user if they wish to repeat the operation
    # The user will be prompted for "y" or "n", but
    # any choice other than "y" will result in the
    # loop being terminated
    repeat_operation = input("Do you want to repeat the operation (y/n): ")
