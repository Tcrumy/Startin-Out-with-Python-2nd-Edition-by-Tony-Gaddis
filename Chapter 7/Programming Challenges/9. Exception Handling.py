# Modify the program that you wrote for Exercise 6 so it handles the following
# exceptions:
# • It should handle any IOError exceptions that are raised when the file is
# opened and data is read from it.
# • It should handle any ValueError exceptions that are raised when the items
# that are read from the file are converted to a number.

def main():

    # This outer try/except block will terminate the program
    # if the chosen file cannot be found.
    try:
        num_file = open("numbers.txt", "r")

        num_of_numbers = 0
        sum_of_numbers = 0

        # This inner try/except block will terminate the program
        # if there is a line that cannot be converted to an int
        try:
            for line in num_file:
                num_of_numbers += 1;
                sum_of_numbers += int(line)

            print("Average:", sum_of_numbers/num_of_numbers)

        # Display message to the user telling them
        # which line of the file has bad data
        except ValueError:
            print("An error occured for line", num_of_numbers)

    # Display message to user letting them know the file
    # Couldn't be found
    except IOError:
        print("IO Error: File could not be found")

main()
