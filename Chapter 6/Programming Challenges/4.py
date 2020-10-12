# The following formula can be used to determine the distance an object falls
# due to gravity in a specific time period, starting from rest:
#          d = 1⁄2 gt^2
# The variables in the formula are as follows: d is the distance in meters, g is
# 9.8, and t is the amount of time in seconds, that the object has been falling.
# Write a function named falling_distance that accepts an object’s falling time
# in seconds as an argument. The function should return the distance in meters
# that the object has fallen during that time interval. Write a program that
# calls the function in a loop that passes the values 1 through 10 as arguments
# and displays the return value.


def main():

    # Display the falling distance for 1 through 10 seconds
    for time in range(1,11):
        print("Second/s: ", time, "   Fall Distance: ", falling_distance(time))

# This function will accept an int argument t that
# represents a time in seconds
# This distance an object falls in that time will be returned
def falling_distance(t):
    return .5 * 9.8 * t**2

main()
