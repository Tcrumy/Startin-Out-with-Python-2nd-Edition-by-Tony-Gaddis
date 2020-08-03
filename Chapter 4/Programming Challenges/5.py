# The colors red, blue, and yellow are known as the primary colors because they
# cannot be made by mixing other colors. When you mix two primary colors, you
# get a secondary color, as shown here:
#   When you mix red and blue, you get purple.
#   When you mix red and yellow, you get orange.
#   When you mix blue and yellow, you get green.
# Design a program that prompts the user to enter the names of two primary
# colors to mix. If the user enters anything other than “red,” “blue,” or
# “yellow,” the program should display an error message. Otherwise, the program
# should display the name of the secondary color that results.

# Prompt user for two colors, chosen from red, blue, or yellow
color1 = input("Color 1 Choose from the colors 'red', 'blue', or 'yellow': ")
color2 = input("Color 2 Choose from the colors 'red', 'blue', or 'yellow': ")

# Use an if-elif-else structure to determing the color
# resulting from the combination of color1 and color2
if ((color1 == "red" and color2 == "blue") or
    (color1 == "blue" and color2 == "red")):

        combined_color = "purple"

elif((color1 == "yellow" and color2 == "blue") or
    (color1 == "blue" and color2 == "yellow")):

        combined_color = "green"

elif((color1 == "yellow" and color2 == "red") or
    (color1 == "red" and color2 == "yellow")):

        combined_color = "orange"

# If the colors are the same and are a valid choice, then
# the combined color will be the same as either color choice
elif((color1 == color2) and
     (color1 == "red" or color1 == "blue" or color1 == "yellow")):

        combined_color = color1

# User entered an invalid color choice
else:
    combined_color = "unknown"

# Use an if-else structure to determing appropriate
# informatio to display to the user
if combined_color == "unknown":
    print("You entered an invalid color choice")

else:
    print("The secondary color is", combined_color)
    
    
    
        
