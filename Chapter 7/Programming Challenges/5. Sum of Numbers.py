# Assume that a file containing a series of integers is named numbers.txt and
# exists on the computer’s disk. Write a program that reads all of the numbers
# stored in the file and calculates their total.

def main():

    # Open the file
    num_file = open("numbers.txt")

    # Read the first line of the file
    line = num_file.readline()

    # Initialize an accumulator for the sum of the integers in the file
    sum = 0

    while line != "":

        # Convert the number string into an int
        num = int(line)

        # Add the number to sum
        sum += num

        # Read the next line
        line = num_file.readline()

    # Display the sum
    print("Sum:",sum)

main()
