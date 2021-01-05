# Write a program that opens the my_name.txt file that was created by the
# program in question 1, reads your name from the file, displays the name on the
# screen, and then closes the file.

def main():

    # Open the file
    name_file = open('my_name.txt', 'r')

    # Print the name in the file
    print(name_file.readline())

    # Close the file
    name_file.close()

main()
