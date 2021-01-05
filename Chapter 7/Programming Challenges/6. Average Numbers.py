# Assume that a file containing a series of integers is named numbers.txt and
# exists on the computer’s disk. Write a program that calculates the average of
# all the numbers stored in the file.

def main():

    # Open the file
    num_file = open("numbers.txt")

    # Read the first line of the file
    line = num_file.readline()

    # Initialize an accumulator for the sum of the integers in the file
    # and an accumulator to the total quantity of numbers stored in the file
    sum = 0
    num_of_nums = 0

    while line != "":

        # Convert the number string into an int
        num = int(line)

        # Add the number to sum and add 1.0 to num_of_nums
        sum += num
        num_of_nums += 1.0

        # Read the next line
        line = num_file.readline()

    # Display the sum
    print("Average:", sum/num_of_nums)

main()
