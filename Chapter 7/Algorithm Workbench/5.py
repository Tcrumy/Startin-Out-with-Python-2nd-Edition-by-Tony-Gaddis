# Modify the code that you wrote in question 4 so it adds all of the numbers
# read from the file and displays their total.

def main():

    # Open the file
    num_file = open('number_list.txt', 'r')

    # Read a line
    line = num_file.readline()

    # Convert the string to an integer
    num = int(line)

    # Create a variable to hold the sum of the integers
    sum = num
    
    # Read and display all numbers in file
    while line != "":
        
        line = num_file.readline()

        if line != "":
            num = int(line)

            sum += num              
        

    # Close file
    num_file.close()

    # Display the sum
    print(sum)
    

main()
