# Write code that does the following: opens the number_list.txt file that was
# created by the code you wrote in question 3, reads all of the numbers from the
# file and displays them, and then closes the file.

def main():

    # Open the file
    num_file = open('number_list.txt', 'r')

    # Read a line
    line = num_file.readline()
    
    # Read and display all numbers in file
    while line != "":
        print(line, end = "")
        line = num_file.readline()

    # Close file
    num_file.close()

main()
