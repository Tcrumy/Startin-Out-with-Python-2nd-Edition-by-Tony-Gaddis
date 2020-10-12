# Write a function named maximum that accepts two integer values as arguments
# and returns the value that is the greater of the two. For example, if 7 and
# 12 are passed as arguments to the function, the function should return 12.
# Use the function in a program that prompts the user to enter two integer
# values. The program should display the value that is the greater of the two.

def main():

    # Prompt user to enter two numbers
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    # Use the maximum function to find the larger value
    larger_num = maximum(num1,num2)

    # Display the larger number to the user
    print(larger_num, "Is the larger value")


# This function will accept two int values
# and will return the larger of the  two
def maximum(a,b):
    if a > b:
        return a
    else:
        return b

main()
