# Create a change-counting game that gets the user to enter the number of coins
# required to make exactly one dollar. The program should prompt the user to
# enter the number of pennies, nickels, dimes, and quarters. If the total value
# of the coins entered is equal to one dollar, the program should congratulate
# the user for winning the game. Otherwise, the program should display a message
# indicating whether the amount entered was more than or less than one dollar.

# Display a message to let the user know what is required
# to win the game
print("You will be prompted to enter a number for four coin types.")
print("In order to win the game, the total value of the coins must")
print("equal exactly one dollar\n")

# Prompt user for number of coins
quarters = int(input("Enter the number of quaters: "))

dimes = int(input("Enter the number of dimes: "))

nickles = int(input("Enter the number of nickles: "))

pennies = int(input("Enter the number of pennies: "))

# Calculate the value in cents for each coin, then total the values together
quarter_value = quarters * 25

dime_value = dimes * 10

nickle_value = nickles * 5

# The penny value in cents will just be the
# amount of pennies entered by the user
penny_value = pennies

total_value_in_cents = (quarter_value + dime_value +
                        nickle_value + penny_value)

# Calculate the value in dollars
dollar_amount = total_value_in_cents / 100

# Use if-elif-else decision structure to determing the
# correct message to display to the user
if dollar_amount == 1.00:
    print("Congratulations, you won the game!")
elif dollar_amount > 1.00:
    print("You lost the game. You total is more than one dollar, try again later.")
else:
    print("You lost the game. You total is less than one dollar, try again later.")
    
