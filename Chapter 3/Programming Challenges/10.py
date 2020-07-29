# A retail company must file a monthly sales tax report listing the total sales
# for the month, and the amount of state and county sales tax collected. The
# state sales tax rate is 4 percent and the county sales tax rate is 2 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:
# • The amount of county sales tax
# • The amount of state sales tax
# • The total sales tax (county plus state)

# Define main
def main():

    monthly_sales = get_month_sales()

    county_tax = calculate_county_tax(monthly_sales)

    state_tax = calculate_state_tax(monthly_sales)

    total_tax = calculate_total_tax(county_tax, state_tax)

    display_info(county_tax, state_tax, total_tax)


# This function will accept no arguments
# The user will be prompted to enter total sales for the month
# The value will be returned as a float
def get_month_sales():

    sales = float(input("Enter sales this month: "))
    return sales

# This function will accept one float argument
# The county tax will be calculated and returned
# as a float
def calculate_county_tax(sales):

    county_tax_rate = .02
    return sales * county_tax_rate

# This function will accept one float argument
# The state tax will be calculated and returned
# as a float
def calculate_state_tax(sales):

    state_tax_rate = .04
    return sales * state_tax_rate

# This function will accept two float arguments
# The tax costs will be added together
# The result will be returned as a float
def calculate_total_tax(county_tax, state_tax):

    return county_tax + state_tax

# This function will accept three arguments
# The arguments will be itemized and displayed
# to the used formatted to two decimal places
# Nothing will be returned
def display_info(state_tax, county_tax, total_tax):

    print("State tax:  ", format(state_tax, ',.2f'))
    print("County tax: ", format(county_tax, ',.2f'))
    print("Total tax:  ", format(total_tax, ',.2f'))

# call main
main()
