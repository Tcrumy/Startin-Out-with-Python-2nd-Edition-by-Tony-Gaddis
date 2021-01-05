# The distance a vehicle travels can be calculated as follows:
#                   distance = speed * time
# For example, if a train travels 40 miles per hour for three hours, the
# distance traveled is 120 miles. Write a program that asks the user for the
# speed of a vehicle (in miles per hour) and the number of hours it has traveled
# It should then use a loop to display the distance the vehicle has traveled for
# each hour of that time period. Here is an example of the desired output:
# What is the speed of the vehicle in mph? 40e
# How many hours has it traveled? 3e
# Hour    Distance Traveled
# 1       40
# 2       80
# 3       120

# Prompt user for speed of vehicle in MPH and time traveled in hours
speed = int(input("What is the speed of the vehicle in mph: "))
time = int(input("How many hours has it taveled: "))

# Display table header
print("Hour    Distance Traveled")
print("-------------------------")

# Write for loop to perform the needed number of iterations
for hour in range(time):
    print(hour + 1, "     ", (hour + 1) * speed)


    
