# This exercise assumes you have completed Programming Exercise 7, Random Number
# File Writer. Write another program that reads the random numbers from the file
# display the numbers, and then display the following data:
#       • The total of the numbers
#       • The number of random numbers read from the file


def main():

    # Open the random numbers file as read
    num_file = open("randomNumbers.txt","r")

    # Initialize accumulators to hold the quantity of numbers in the file
    # and another to hold the sum of the numbers in the file
    num_of_numbers = 0
    sum_of_numbers = 0

    # Add one to quantity of numbers accumulator
    # and add the number to the sum of numbers accumulator
    for line in num_file:
        
        print(line, end = "")
        num_of_numbers +=1
        sum_of_numbers += int(line)

    # Display results to the user
    print("Sum:", sum_of_numbers)
    print("QTY of Numbers:", num_of_numbers)

# Call main 
main()
