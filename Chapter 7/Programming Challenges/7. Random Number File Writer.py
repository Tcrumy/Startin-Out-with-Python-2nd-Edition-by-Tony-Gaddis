# Write a program that writes a series of random numbers to a file. Each random
# number should be in the range of 1 through 100. The application should let the
# user specify how many random numbers the file will hold.

import random

def main():

    rand_num_file = open("randomNumbers.txt","w")

    # Ask user how many random numbers to generate
    nums_to_generate = int(input("Enter the quantity of numebrs to generate: "))

    # Write user requested quantity of random numbers to file
    for num in range(nums_to_generate):

        rand_num_file.write(str(random.randint(0,100)) + "\n")

main()
