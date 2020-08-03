# The date June 10, 1960, is special because when it is written in the
# following format, the month times the day equals the year:
#                     6/10/60
# Design a program that asks the user to enter a month (in numeric form),
# a day, and a two digit year. The program should then determine whether the
# month times the day equals the year. If so, it should display a message saying
# the date is magic. Otherwise, it should display a message saying the date is
# not magic.

# Prompt user for month as a digit 1-12
month = int(input("Enter the month as a digit 1-12: "))

# Prompt user for day as a digit 1-31
day = int(input("Enter the day as a digit 1-31: "))

# Prompt the user for the year as a two digit number
year = int(input("Enter the year as a two digit number ex.(1960 = 60): "))

# Use an if-else structure to determine if
# the date is a magic date and display this
# to the user
if month * day == year:
    print("The date is magic.")

else:
    print("The date is not magic.")
