# Write a program that asks the user for the name of a file. The program should
# display only the first five lines of the file’s contents. If the file contains
# less than five lines, it should display the file’s entire contents.

def main():

    # Prompt user for the file name
    file_name = input("Enter the name of the file: ")

    # Open the file
    file = open(file_name,'r')
    
    # Initialize an accumulator
    num_of_line = 0

    # Display all lines up to and including line 5    
    for line in file:
        
        if num_of_line <= 4:
            print(line, end = "")
        else:
            break

        num_of_line += 1


main()
