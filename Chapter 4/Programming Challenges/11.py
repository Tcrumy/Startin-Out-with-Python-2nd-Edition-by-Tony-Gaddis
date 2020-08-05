# Write a program that asks the user to enter a number of seconds, and works as
# follows:
#    • There are 60 seconds in a minute. If the number of seconds entered by
#      the user is greater than or equal to 60, the program should display the
#      number of minutes in that many seconds.
# 
#    • There are 3,600 seconds in an hour. If the number of seconds entered by
#      the user is greater than or equal to 3,600, the program should display
#      the number of hours in that many seconds.
# 
#    • There are 86,400 seconds in a day. If the number of seconds entered by
#      the user is greater than or equal to 86,400, the program should display
#      the number of days in that many seconds.

# NOTE: Even though chapter 4 isn't on functions, we'll write this
# one with functions for practice. Also, the requirements don't ask
# us to handle a situation in which the seconds entered is less than
# 60, but we'll add it anyway

# Define Main
def main():

    seconds = get_seconds()

    calculation_type = define_calculation_type(seconds)

    result_from_conversion = convert_seconds_to_appropriate_type(seconds, calculation_type)

    display_info(seconds, result_from_conversion, calculation_type)

    
    

# This function has no arguments
# The user will be prompted to enter a number
# for seconds
# This number will be returned as an int
def get_seconds():

    seconds = int(input("Enter a number for seconds greater than 59: "))

    return seconds

# This function accepts an int argument for seconds
# The appropriate calculation type will be determined
# based on the number entered
# The calculation type will be returned as a string
def define_calculation_type(seconds):

    if seconds >= 86400:
        calculation_type = "days"
    elif seconds >= 3600 and seconds < 86400:
        calculation_type = "hours"
    elif seconds >= 60 and seconds < 3600:
        calculation_type = "minutes"
    else:
        calculation_type = "no calculation"

    return calculation_type

# This function accepts two arguments, a string and an int
# The seconds will be converted to minutes, hours, or days
# depending on what the calculation type is
# The result will be returned as a float
def convert_seconds_to_appropriate_type(seconds, calc_type):

    if calc_type == "days":
        result = seconds / 86400
    elif calc_type == "hours":
        result = seconds / 3600
    elif calc_type == "minutes":
        result = seconds / 60
    else:
        result = seconds

    return result

# This function will accept three arguments, two ints and a string
# A message will be displayed showing the appropriate conversion
# of the number of seconds
# Nothing is returned.
def display_info(seconds, converted_number, calc_type):

    if calc_type == "days":
        print(seconds, "seconds is", converted_number, "day/s")
    elif calc_type == "hours":
        print(seconds, "seconds is", converted_number, "hour/s")
    elif calc_type == "minutes":
        print(seconds, "seconds is", converted_number, "minute/s")
    else:
        # This is unnecessary, but we'll add it anyway
        print(seconds, "seconds is", converted_number, "second/s")

# call main
main()
        
