# Write a program that calculates the total amount of a meal purchased at a
# restaurant. The program should ask the user to enter the charge for the food,
# and then calculate the amount of a 15 percent tip and 7 percent sales tax.
# Display each of these amounts and the total.

# Create variables to store the sales tax rate as a percentage
tax_rate = 0.07

# Create a variable to store the tip rate as a percentage
tip_rate = 0.15

# Prompt user for subtotal
subtotal = float(input("Enter subtotal: "))

# Calculate tax
sales_tax = subtotal * tax_rate

# Calculate tip
tip = subtotal * tip_rate

# Calculate total
total = subtotal + tip + sales_tax

# Display information to user formatted to 2 decimal places
print("Subtotal: ", format(subtotal, ",.2f"))
print("Tax:      ", format(sales_tax, ",.2f"))
print("Tip:      ", format(tip, ",.2f"))
print("Total:    ", format(total, ",.2f"))
