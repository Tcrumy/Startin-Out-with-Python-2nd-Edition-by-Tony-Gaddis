# Suppose you have a certain amount of money in a savings account that earns
# compound monthly interest and you want to calculate the amount that you will
# have after a specific number of months. The formula is
#                   F = P * (1 + i)^t
# The terms in the formula are as follows:
# • F is the future value of the account after the specified time period.
# • P is the present value of the account.
# • i is the monthly interest rate.
# • t is the number of months.
# Write a program that prompts the user to enter the account’s present value,
# monthly interest rate, and number of months that the money will be left in the
# account. The program should pass these values to a function that returns the
# future value of the account after the specified number of months. The program
# should display the account’s future value.

def main():

    # Prompt user for accounts present value,
    # monthly interest rate, and number of months
    # the money will be in the account
    P = float(input("Enter accounts present value: "))
    i = float(input("Enter the monthly interest rate: "))/100
    t = int(input("Enter the number of months the money will be in the account: "))

    F = calculate_future_value(P, i, t)

    print("Future value: ", format(F, ",.2f"))

# This function will accept three integer arguments for
# based on these numbers the future value of the users
# account will be calculated
def calculate_future_value(P, i, t):

    future_value = P * (1 + i) ** t

    return future_value

main()
