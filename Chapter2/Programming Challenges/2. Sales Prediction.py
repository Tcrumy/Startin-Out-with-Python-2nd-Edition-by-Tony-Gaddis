# A company has determined that its annual profit is typically 23 percent 
# of total sales. Write a program that asks the user to enter the projected 
# amount of total sales, and then displays the profit that will be made
# from that amount.
# Hint: use the value 0.23 to represent 23 percent.

# NOTE: This is an excellent example of an input, processing, output program
# There are three distinct areas that handle each task. I will mark each one

#############################################################
# Input
#############################################################
# Create a variable to hold the profit percentage
profit_percentage = 0.23

# Prompt the user to enter the projected total sales
projected_sales = float(input("Enter projected total sales: "))

############################################################
# Processing
############################################################
# Calculate the the profit from the sales
profit = projected_sales * profit_percentage

############################################################
# Output
############################################################
# Display the profit to the user
print(profit)

            
