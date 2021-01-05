# One acre of land is equivalent to 43,560 square feet. Write a program
# that asks the user to enter the total square feet in a tract of
# land and calculates the number of acres in the tract.
# Hint: divide the amount entered by 43,560 to get the number of acres.

# Create a variable to hold amout of square feet per acre
sqft_per_acre = 43560

# Prompt user for input of land area in square feet
land_sqft = float(input("Enter land area in sqaure feet: "))

# Convert from square feet to acres
acres = land_sqft / sqft_per_acre

# Display information to user
print(land_sqft, "square feet is", acres, "acres.")
