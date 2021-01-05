# Scientists measure an object’s mass in kilograms and its weight in newtons.
# If you know the amount of mass of an object in kilograms, you can calculate
# its weight in newtons with the following formula:
#                   weight = mass x 9.8
# Write a program that asks the user to enter an object’s mass, and then
# calculates its weight. If the object weighs more than 1,000 newtons, display
# a message indicating that it is too heavy. If the object weighs less than 10
# newtons, display a message indicating that it is too light.

# Prompt user to enter mass in kilograms
mass = int(input("Enter mass in kilograms: "))

# Calculate weight in newtons using the formula weight = mass x 9.8
weight = mass * 9.8

# Use an if-elif-else structure to notify the user
# as to whether the object is too heavy or too light
if weight > 1000:
    print("Object is too heavy.")

elif weight < 10:
    print("Object is too light.")

else:
    print("Object is neither too heavy, not too light.")
