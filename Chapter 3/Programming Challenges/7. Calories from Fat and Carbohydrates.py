# A nutritionist who works for a fitness club helps members by evaluating their
# diets. As part of her evaluation, she asks members for the number of fat grams
# and carbohydrate grams that they consumed in a day. Then, she calculates the
# number of calories that result from the fat, using the following formula:
#                 calories from fat = fat grams x 9
# Next, she calculates the number of calories that result from the carbohydrates
# , using the following formula:
#                calories from carbs = carb grams x 4
# The nutritionist asks you to write a program that will make these calculations

# Define main
def main():

    fat_grams = get_fat_grams()
    
    carb_grams = get_carb_grams()

    fat_calories = calculate_fat_calories(fat_grams)

    carb_calories = calculate_carb_calories(carb_grams)

    display_info(fat_calories, carb_calories)
    
# This function accepts no arguments
# The user will be prompted to enter the number
# of fat grams they consume daily
# The value will be returned as a float
def get_fat_grams():
    daily_fat_grams = float(input("Enter daily fat grams consumed: "))
    return daily_fat_grams

# This function accepts no arguments
# The user will be prompted to enter the number
# of carb grams they consume daily
# The value will be returned as a float
def get_carb_grams():
    carb_grams = float(input("Enter daily carb grams consumed: "))
    return carb_grams

# This function accepts one float argument
# The given value will be used to calculate
# fat calories consumed by the user
# This number will be returned as a float
def calculate_fat_calories(fat_grams):

    # The formula for calculating fat calories is fat calories = fat grams * 9
    return fat_grams * 9

# This function accepts one float argument
# The given value will be used to calculate
# carb calories consumed by the user
# This number will be returned as a float
def calculate_carb_calories(carb_grams):

    # The formula for calculating carb calories is
    # carb calories = carb grams * 4
    return carb_grams * 4

# NOTE: The challenge does not ask for a function to display the info
#       but I will write one anyway

# This function will accept two float arguments
# The number of fat calories and carb calories
# consumed by the user will be displayed
# Nothing will be returned
def display_info(fat_calories, carb_calories):
    print("Fat calories:  ", format(fat_calories, ',.2f'))
    print("Carb calories: ", format(carb_calories, ',.2f'))

# Call main
main()
