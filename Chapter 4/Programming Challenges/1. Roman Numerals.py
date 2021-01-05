# Write a program that prompts the user to enter a number within the range of 1
# through 10. The program should display the Roman numeral version of that
# number. If the number is outside the range of 1 through 10, the program
# should display an error message. The following table shows the Roman
# numerals for the numbers 1 through 10:

"""
    Number Roman Numeral
    1            I
    2            II
    3            III
    4            IV
    5            V
    6            VI
    7            VII
    8            VIII
    9            IX
    10           X
"""

# Prompt for number choice
number_choice = int(input("Enter a number 1-10: "))

# This if-elif structure will handle the numbers 1 through 10
# but if the user enters some other number, nothing will be displayed
if number_choice == 1:
    print("I")
    
elif number_choice == 2:
    print("II")
    
elif number_choice == 3:
    print("III")
    
elif number_choice == 4:
    print("IV")
    
elif number_choice == 5:
    print("V")
    
elif number_choice == 6:
    print("VI")
    
elif number_choice == 7:
    print("VII")
    
elif number_choice == 8:
    print("VIII")
    
elif number_choice == 9:
    print("IX")
    
elif number_choice == 10:
    print("X")
