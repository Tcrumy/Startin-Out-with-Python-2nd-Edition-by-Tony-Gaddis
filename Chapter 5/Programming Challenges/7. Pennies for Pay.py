# Write a program that calculates the amount of money a person would earn over
# a period of time if his or her salary is one penny the first day, two pennies
# the second day, and continues to double each day. The program should ask the
# user for the number of days. Display a table showing what the salary was for
# each day, and then show the total pay at the end of the period. The output
# should be displayed in a dollar amount, not the number of pennies.

# Prompt user for number of days worked
days_worked = int(input("Enter number of days worked: "))

# set pay at one penny
pay = .01

# Display table header
print("Day        Pay")
print("----------------")

for day in range(1, days_worked + 1):
    print(format(day, "2d"), format(pay, "13,.2f"))
    pay *= 2
