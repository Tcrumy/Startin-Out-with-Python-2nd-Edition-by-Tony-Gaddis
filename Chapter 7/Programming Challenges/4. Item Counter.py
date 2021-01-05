# Assume that a file containing a series of names (as strings) is named
# names.txt and exists on the computer’s disk. Write a program that displays
# the number of names that are stored in the file. (Hint: Open the file and
# read every string stored in it. Use a variable to keep a count of the number
# of items that are read from the file.)

def main():

    # Open the file
    name_file = open("names.txt", "r")

    # Initialize an accumulator to hold number of names
    num_of_names = 0

    # Add one to number of names for every name in the file
    for line in name_file:

        if line != "\n":
            num_of_names += 1

    # Display the number of names in the file
    print("There are", num_of_names, "names on the file.")
    
main()
