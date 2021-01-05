# Write a program that opens an output file with the filename my_name.txt,
# writes your name to the file, and then closes the file.

def main():

    # Open the file
    name_file = open("my_name.txt", 'w')

    # Write your name to the file
    name_file.write("My name")

    # Close the file
    name_file.close()

main()
