# The area of a rectangle is the rectangle’s length times its width. Write a
# program that asks for the length and width of two rectangles. The program
# should tell the user which rectangle has the greater area, or if the areas
# are the same.

# Prompt user for length and width of the first rectangle
length1 = int(input("Enter the length of rectangle 1: "))
width1 = int(input("Enter the width of rectangle 1: "))

# Prompt user for length and width of the second rectangle
length2 = int(input("Enter the length of rectangle 2: "))
width2 = int(input("Enter the width of rectangle 2: "))

# Calculate the areas of each triangle
area1 = length1 * width1
area2 = length2 * width2

# Use an if else structure to determing which
# rectangle has the largest area, and display
# that information to the user
if area1 > area2:
    print("Rectangle 1 is larger.")

elif area2 > area1:
    print("Rectangle 2 is larger")

# If this else is executed, the rectangles are the same size
else:
    print("Rectangle 1 and rectangle 2 are the same size")
