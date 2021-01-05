# A software company sells a package that retails for $99. Quantity discounts
# are given according to the following table:
#           Quantity            Discount
#           10–19               20%
#           20–49               30%
#           50–99               40%
#           100 or more         50%
# Write a program that asks the user to enter the number of packages purchased.
# The program should then display the amount of the discount (if any) and the
# total amount of the purchase after the discount.

# Setup global variable for package price
PACKAGE_PRICE = 99

# Prompt user for number of packages they wish to purchase
packages_purchased = int(input("Enter the purchase quantity for packages: "))

# Use if-elif-else to determine the correct discount to apply
# The discounted percentage will be 1.00 minus the discount
# so a 20% discount will have a discounted percentage of .80
# because 1.00 - .20 = .80
if packages_purchased >= 100:
    discounted_percentage = .50
elif packages_purchased >= 50 and packaged_purchased <= 99:
    discounted_percentage = .60
elif packages_purchased >= 20 and packaged_purchased <= 49:
    discounted_percentage = .70
elif packages_purchased >= 10 and packaged_purchased <= 19:
    discounted_percentage = .80
else:
    discounted_percentage = 1.00

# Calculate the total price and the price after the discount is applies
total_price = packages_purchased * PACKAGE_PRICE

discounted_price = total_price * discounted_percentage

# Display message to user
print("Your discount is %", (1.00 - discounted_percentage) * 100,"." , sep="")
print("Your discounted price is $", format(discounted_price, ",.2f"), sep="")


