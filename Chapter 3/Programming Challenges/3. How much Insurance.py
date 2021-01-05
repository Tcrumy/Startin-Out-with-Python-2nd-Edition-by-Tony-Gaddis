# Many financial experts advise that property owners should insure their homes or
# buildings for at least 80 percent of the amount it would cost to replace the
# structure. Write a program that asks the user to enter the replacement cost of
# a building and then displays the minimum amount of insurance he or she should
# buy for the property.

# This function has no parameters
# The user will be prompted to enter a replacement cost for
# a given structure, and this cost will be returned as a float
def get_replacement_cost():
    replacement_cost = float(input("Enter cost for replacement of structure: "))
    return replacement_cost

# This function accepts one float parameter for a structures replacement cost
# A calculation will be performed on the input to determine the appropriate
# amount of insurance coverage for the given data. The result will be returned
# as a float
def calculate_insurance_coverage(replacement_cost):
    suggested_coverage_percentage = 0.8
    suggested_coverage = replacement_cost * suggested_coverage_percentage
    return suggested_coverage

def main():

    replacement_cost = get_replacement_cost()

    suggested_coverage = calculate_insurance_coverage(replacement_cost)

    # Display the results to the user
    print("For a structure that costs", format(replacement_cost, ",.2f"),"to replace," )
    print(format(suggested_coverage,",.2f"), "is your recommended minimum coverage amount.")

main()
