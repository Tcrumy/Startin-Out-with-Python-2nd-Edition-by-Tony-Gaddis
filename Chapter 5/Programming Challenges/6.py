# Write a program that displays a table of the Celsius temperatures 0 through 20
# and their Fahrenheit equivalents. The formula for converting a temperature
# from Celsius to Fahrenheit is:
#  F = (9/5) * C + 32
# where F is the Fahrenheit temperature and C is the Celsius temperature. Your
# program must use a loop to display the table.

# Display table header
print("Celsius    Fahrenheit")
print("---------------------")

for celsius in range(21):
    fah = (9/5) * celsius + 32
    print(celsius ,"          ", fah )

