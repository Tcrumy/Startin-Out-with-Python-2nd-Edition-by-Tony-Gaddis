# Programming Exercise #6 in Chapter 2 was the Sales Tax program. For that
# exercise you were asked to write a program that calculates and displays the
# county and state sales tax on a purchase. If you have already written that
# program, redesign it so the subtasks are in functions. If you have not
# already written that program, write it using functions.

def get_purchase_amount():
    purchase_amount = float(input("Enter Purchase amount: "))
    return purchase_amount

def calculate_state_tax(subtotal):
    state_tax_rate = 0.04
    return subtotal * state_tax_rate

def calculate_count_tax(subtotal):
    county_tax_rate = 0.02
    return subtotal * county_tax_rate

def calculate_total(subtotal, county_tax, state_tax):
    return subtotal + county_tax + state_tax

def display_info(subtotal, county_tax, state_tax, total):
    print("Subtotal:  ", format(subtotal, ",.2f"))
    print("County Tax:", format(county_tax, ",.2f"))
    print("State Tax: ", format(state_tax, ",.2f"))
    print("Total:     ", format(total, ",.2f"))

def main():
    subtotal = get_purchase_amount()

    state_tax = calculate_state_tax(subtotal)

    county_tax = calculate_count_tax(subtotal)

    total = calculate_total(subtotal, county_tax, state_tax)

    display_info(subtotal, county_tax, state_tax, total)

main()
