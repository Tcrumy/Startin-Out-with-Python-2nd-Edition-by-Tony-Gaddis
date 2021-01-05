# A car’s miles-per-gallon (MPG) can be calculated with the following formula:
# MPG = miles driven/Gallons of gas used
# Write a program that asks the user for the number of miles driven and the
# gallons of gas used. It should calculate the car’s MPG and display the result.

# Prompt user for miles driven
miles_driven = float(input("Enter miles driven: "))

# Prompt user for gallons of gas used
gallons_used = float(input("Enter gallons of gas use: "))

# Calculate gas milage
gas_milage = miles_driven / gallons_used

# Display information to user
print("Your fuel efficiency is", gas_milage, "miles per gallon." )
