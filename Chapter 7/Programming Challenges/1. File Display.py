# Assume that a file containing a series of integers is named numbers.txt and
# exists on the computer’s disk. Write a program that displays all of the
# numbers in the file.

def main():

    # Open the file
    num_file = open('numbers.txt', 'r')

    # Assign the value of the fist line to num
    line = num_file.readline()

    # Read and display line until the end of the file
    while line != "":

        print(line, end = "")
        line = num_file.readline()

main()
