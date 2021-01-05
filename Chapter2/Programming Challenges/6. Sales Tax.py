# Write a program that will ask the user to enter the amount of a purchase.
# The program should then compute the state and county sales tax. Assume the
# state sales tax is 4 percent and the county sales tax is 2 percent. The
# program should display the amount of the purchase, the state sales tax, the
# county sales tax, the total sales tax, and the total of the sale(which is the
# sum of the amount of purchase plus the total sales tax).
# Hint: use the value 0.02 to represent 2 percent, and 0.04 to represent 4 percent.

# Create two variables to hold the county and state sales tax rate respectivly
county_tax_rate = .02
state_tax_rate = .04

# Prompt user to enter amount of purchase. This will be the subtotal since
# only one item/purchase amount is being asked for
subtotal = float(input("Enter Purchase Amount: "))

# Calculate county and state tax
county_tax = subtotal * county_tax_rate
state_tax = subtotal * state_tax_rate

# Calculate total sales tax
total_sales_tax = county_tax + state_tax

# Calculate total
total = subtotal + county_tax + state_tax

# Display information to the user formated to 2 decimal places
print("Subtotal:  ", format(subtotal, ",.2f"))
print("State tax: ", format(state_tax, ",.2f"))
print("County tax:", format(county_tax, ",.2f"))
print("Total tax: ", format(total_sales_tax, ",.2f"))
print("Total:     ", format(total, ",.2f"))
