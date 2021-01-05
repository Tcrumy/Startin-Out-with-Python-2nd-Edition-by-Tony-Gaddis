# Write a program that asks the user for the name of a file. The program should
# display the contents of the file with each line preceded with a line number
# followed by a colon. The line numbering should start at 1.

def main():

    # Prompt user for the file name
    file_name = input("Enter the name of the file: ")

    # Open the file
    file = open(file_name,'r')

    # Initialize an accumulator
    line_num = 1
    
    # Display all lines with the preceding line number
    for line in file:

        if line != "\n":
            print(line_num, ": " , line, sep="", end = "")
            
        line_num += 1
        
main()
