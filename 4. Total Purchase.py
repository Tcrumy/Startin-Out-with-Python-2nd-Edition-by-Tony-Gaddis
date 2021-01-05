# A customer in a store is purchasing five items. Write a program that asks for +
# the price of each item, and then displays the subtotal of the sale, the amount
# of sales tax, and the total. Assume the sales tax is 6 percent.

# Create a variable to store the tax rate as a percentage
tax_rate = .06

# Create 5 seperate item variables to store the price of each item via user prompt
item1_price = float(input("Enter Item 1 Price: "))
item2_price = float(input("Enter Item 2 Price: "))
item3_price = float(input("Enter Item 3 Price: "))
item4_price = float(input("Enter Item 4 Price: "))
item5_price = float(input("Enter Item 5 Price: "))

# Calculate subtotoal
subtotal = item1_price + item2_price + item3_price + item4_price + item5_price

# Calculate sales tax
sales_tax = subtotal * tax_rate

# Claculate total
total = subtotal + sales_tax

# Display information to the user formated to 2 decimal places
print("Subtotal:", format(subtotal, ",.2f"))
print("Tax:     ", format(sales_tax, ",.2f"))
print("Total:   ", format(total, ",.2f"))

