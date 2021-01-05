# Write code that does the following: opens an output file with the filename
# number_list.txt, uses a loop to write the numbers 1 through 100 to the file,
# and then closes the file.

def main():

    # open the file
    num_file = open('number_list.txt', 'w')

    # Write the numbers 1 - 100 to the file
    for num in range(1,101):
        num_file.write(str(num) + "\n")

    # Close the file
    num_file.close()

main()
