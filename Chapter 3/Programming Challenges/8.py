# There are three seating categories at a stadium. For a softball game, Class A
# seats cost $15, Class B seats cost $12, and Class C seats cost $9. Write a
# program that asks how many tickets for each class of seats were sold, and
# then displays the amount of income generated from ticket sales.

# Define Main
def main():

    class_a_tickets_sold = get_class_a_sold()

    class_b_tickets_sold = get_class_b_sold()

    class_c_tickets_sold = get_class_c_sold()

    ticket_income = calculate_ticket_income(class_a_tickets_sold,
                                            class_b_tickets_sold,
                                            class_c_tickets_sold)

    display_info(ticket_income)
    
# This function accepts no arguments
# The used will be prompted to enter
# the qty of tickets for the given class
# of seating were sold
# The value will be returned as an int
def get_class_a_sold():

    class_a_sold = int(input("Enter number of class A tickets sold: "))
    return class_a_sold
    
# This function accepts no arguments
# The used will be prompted to enter
# the qty of tickets for the given class
# of seating were sold
# The value will be returned as an int
def get_class_b_sold():

    class_b_sold = int(input("Enter number of class B tickets sold: "))
    return class_b_sold

# This function accepts no arguments
# The used will be prompted to enter
# the qty of tickets for the given class
# of seating were sold
# The value will be returned as an int
def get_class_c_sold():

    class_c_sold = int(input("Enter number of class C tickets sold: "))
    return class_c_sold

# This function will accept three int arguments
# The income generated from ticket sales will be calculated
# The value will be returned as a float
def calculate_ticket_income(class_a_tickets, class_b_tickets, class_c_tickets):

    CLASS_A_PRICE = 15
    CLASS_B_PRICE = 12
    CLASS_C_PRICE = 9

    total_income = (class_a_tickets * CLASS_A_PRICE +
                    class_b_tickets * CLASS_B_PRICE +
                    class_c_tickets * CLASS_C_PRICE )
    return total_income

# This function accepts one float arugument
# The value will be displayed to the user formatted to two decimal places
# The function returns nothing
def display_info(total_ticket_income):

    print("Ticket Income: ", format(total_ticket_income, ',.2f'))

# Call main
main()



    
