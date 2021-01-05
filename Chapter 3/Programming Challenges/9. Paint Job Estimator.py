# A painting company has determined that for every 115 square feet of wall
# space, one gallon of paint and eight hours of labor will be required. The
# company charges $20.00 per hour for labor. Write a program that asks the user
# to enter the square feet of wall space to be painted and the price of the
# paint per gallon. The program should display the following data:
# • The number of gallons of paint required
# • The hours of labor required
# • The cost of the paint
# • The labor charges
# • The total cost of the paint job

# Define Main
def main():

    wall_space = get_wall_space()

    paint_cost_per_gallon = get_paint_cost_per_gallon()

    gallons_of_paint_needed = calculate_paint_needed(wall_space)

    labor_hours_needed = calculate_labor_hours(wall_space)

    labor_cost = calculate_labor_cost(labor_hours_needed)

    total_paint_cost = calculate_paint_cost(gallons_of_paint_needed,
                                            paint_cost_per_gallon)

    paint_job_cost = calculate_paint_job_cost(total_paint_cost, labor_cost)

    display_info(gallons_of_paint_needed, labor_hours_needed, total_paint_cost,
                 labor_cost, paint_job_cost)
    
# This function will accept no arguments
# The user will be prompted to enter
# the wall space in sqft
# This value will be returned as an int
def get_wall_space():

    wall_space = int(input("Enter wall space in square feet: "))

    return wall_space

# This function will accept no arguments
# The user will be prompted to enter
# the cost per gallon of paint
# This value will be returned as a float
def get_paint_cost_per_gallon():

    cost_per_gallon = float(input("Enter paint cost per gallon: "))

    return cost_per_gallon

# This function will accept one int argument
# The wall space to be painted will be used
# to calculate the number of gallons of paint needed
# This number will be returned as a float
def calculate_paint_needed(wall_space):

    # One gallon is needed per 115 square feet of wall space
    gallons_needed = wall_space / 115
    return gallons_needed

# This function will accept one int argument
# The wall space to be painted will be used
# to calculate the number of labor hours for the job
# This number will be returned as a float
def calculate_labor_hours(wall_space):

    # 8 hours of labor is needed per 115 square feet of wall space
    hours_of_labor = (wall_space / 115) * 8
    return hours_of_labor

# This function will accept two float arguments
# The arguments will be used to calculate the total cost of labor
# The value will be returned as a float
def calculate_labor_cost(hours_of_labor, labor_cost = 20):

    return hours_of_labor * labor_cost

# This function will accept two float arguments
# The arguments will be used to calculate the total cost of paint
# The value will be returned as a float
def calculate_paint_cost(gallons_of_paint, cost_per_gallon):

    return gallons_of_paint * cost_per_gallon

# This function will accept two float arguments
# The arguments will be used to calculate the total cost of the paint job
# The value will be returned as a float
def calculate_paint_job_cost(paint_cost, labor_cost):

    return paint_cost + labor_cost


# This function will accept four float arguments
# and one int argument
# These values will be itemized and displayed to the user
# Nothing will be returned
def display_info(gallons_needed, labor_hours_needed, paint_cost,
                 labor_cost, total_cost):

    print("Gallons Of Paint: ", format(gallons_needed, ',.2f'))
    print("Labor Hours:      ", format(labor_hours_needed, ',.2f'))
    print("Paint Cost:       ", format(paint_cost, ',.2f'))
    print("Labor Cost:       ", format(labor_cost, ',.2f'))
    print("Total Cost:       ", format(total_cost, ',.2f'))

# Call main
main()


