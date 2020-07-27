# Write a program that asks the user to enter the monthly costs for the
# following expenses incurred from operating his or her automobile: loan
# payment, insurance, gas, oil, tires, and maintenance. The program should
# then display the total monthly cost of these expenses, and the total annual
# cost of these expenses.



def main():

    loan_cost = get_loan_payment()

    insurance_cost = get_insurance_cost()
    
    gas_cost = get_gas_cost()

    oil_cost = get_oil_cost()

    tire_cost = get_tire_cost()

    maintenance_cost = get_maintenance_cost()

    total_monthly_cost = calculate_total_monthly_cost(loan_cost, insurance_cost,
                                                      gas_cost, oil_cost, tire_cost,
                                                      maintenance_cost)

    total_annual_cost = total_monthly_cost * 12

    print("Your total monthly cost is ", format(total_monthly_cost, ",.2f"))
    print("Your total annual cost is ", format(total_annual_cost, ",.2f"))

# This function has no arguments
# The user will be prompted to enter a loan payment amount
# This amount will be returned as a float
def get_loan_payment():
    loan_payment = float(input("Enter monthly loan payment: "))
    return loan_payment

# This function has no arguments
# The user will be prompted to enter insurance costs
# This amount will be returned as a float
def get_insurance_cost():
    insurance_cost = float(input("Enter monthly insurance cost: " ))
    return insurance_cost

# This function has no arguments
# The user will be prompted to enter gas costs
# This amount will be returned as a float
def get_gas_cost():
    gas_cost = float(input("Enter monthly gas cost: " ))
    return gas_cost

# This function has no arguments
# The user will be prompted to enter oil costs
# This amount will be returned as a float
def get_oil_cost():
    oil_cost = float(input("Enter monthly oil cost: " ))
    return oil_cost

# This function has no arguments
# The user will be prompted to enter tire costs
# This amount will be returned as a float
def get_tire_cost():
    tire_cost = float(input("Enter monthly tire cost: " ))
    return tire_cost

# This function has no arguments
# The user will be prompted to enter maintenance costs
# This amount will be returned as a float
def get_maintenance_cost():
    maintenance_cost = float(input("Enter monthly maintenance cost: " ))
    return maintenance_cost

# This function accepts six float arguments
# These arguments will be summed up
# The summed value will be returned
def calculate_total_monthly_cost(loan, insurance, gas, oil, tire, maintenence):
    total_monthly_cost = loan + insurance + gas + oil + tire + maintenence
    return total_monthly_cost


main()
    
