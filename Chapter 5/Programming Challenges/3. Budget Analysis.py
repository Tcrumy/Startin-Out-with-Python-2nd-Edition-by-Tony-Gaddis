# Write a program that asks the user to enter the amount that he or she has
# budgeted for a month. A loop should then prompt the user to enter each of his
# or her expenses for the month, and keep a running total. When the loop
# finishes, the program should display the amount that the user is over or under
# budget.


# Promput user for monthly budget
monthly_budget = float(input("Enter your monthly budget: "))

# Prompt user for number of expenses
number_of_expenses = int(input("Enter the number of monthly expenses: "))

# Define running total
running_expense_total = 0

# Write for loop to keep a running total of expenses
for expense in range(number_of_expenses):

    print("Enter expense", expense + 1, ": ", end = "")
    cost_of_bill = float(input())

    running_expense_total += cost_of_bill

# Calculate budget difference
budget_difference = monthly_budget - running_expense_total

# Use if-elif-else decision structure to determing message to display to user
if budget_difference > 0:
    print("You are under budget, with $", format(budget_difference, ",.2f"), " left", sep = "")
elif budget_difference < 0:
    print("You are over budget by $", format(-1 * budget_difference, ",.2f"), sep = "")
else:
    print("You have spent your budget, with $", format(budget_difference, ",.2f"), " left", sep = "")
    
