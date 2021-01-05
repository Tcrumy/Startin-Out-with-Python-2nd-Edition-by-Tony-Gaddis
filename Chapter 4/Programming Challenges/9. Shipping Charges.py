# The Fast Freight Shipping Company charges the following rates:
#            Weight of Package                          Rate per Pound
#            2 pounds or less                           $1.10
#            Over 2 pounds but not more than 6 pounds   $2.20
#            Over 6 pounds but not more than 10 pounds  $3.70
#            Over 10 pounds                             $3.80
# Write a program that asks the user to enter the weight of a package and then
# displays the shipping charges.

# Prompt user to enter package weight
package_weight = float(input("Enter package weight in pounds: "))

# User if-elif-else decision structure to determine the charge per pound
if package_weight > 10:
    charge_per_pound = 3.80
elif package_weight > 6 and package_weight <= 10:
    charge_per_pound = 3.70
elif package_weight > 2 and package_weight <= 6:
    charge_per_pound = 2.20
else:
    charge_per_pound = 1.10

# Calculate the total shipping charge
total_shipping_charge = package_weight * charge_per_pound

# Display information to the user
print("Your total shipping charge is $", format(total_shipping_charge, ",.2f"), sep="")
