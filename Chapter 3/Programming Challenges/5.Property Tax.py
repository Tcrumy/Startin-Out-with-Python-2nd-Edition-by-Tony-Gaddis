# A county collects property taxes on the assessment value of property, which is
# 60 percent of the property’s actual value. For example, if an acre of land is
# valued at $10,000, its assessment value is $6,000. The property tax is then
# 64¢ for each $100 of the assessment value. The tax for the acre assessed at
# $6,000 will be $38.40. Write a program that asks for the actual value of a
# piece of property and displays the assessment value and property tax.

# This function accepts no arguments
# The user will be prompted to enter a properties value
# and the value will be returned as a float
def get_property_value():
    value = float(input("Enter Property Value: "))
    return value

# This function will accept a float argument
# The argument will be multiplied by an assessed value rate
# and the product will be returned as a float
def calculate_assessed_value(value):

    # The assessed value is 60 percent of the actual value
    # setup a multiplier variable for the assessed rate
    assessed_rate = .60

    assessed_value = value * assessed_rate

    return assessed_value

# This function will accept a float argument
# The argument will be multiplied by a tax rate
# and the product will be returned as a float
def calculate_tax(assessed_value):

    # The tax rate is 64 cents for every $100, this is .0064%
    tax_rate = .0064

    tax = assessed_value * tax_rate

    return tax

# This function will accept a two float arguments
# The argument will be formatted and displayed per the requirements
def display_info(assessed_value, tax):
    print("Assessed Value:", format(assessed_value,',.2f'))
    print("Tax: ", format(tax,',.2f'))

def main():

    property_value = get_property_value();

    assessed_value = calculate_assessed_value(property_value)

    tax = calculate_tax(assessed_value)

    display_info(assessed_value, tax)

main()
    
