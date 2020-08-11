# Running on a particular treadmill you burn 3.9 calories per minute. Write a
# program that uses a loop to display the number of calories burned after 10,
# 15, 20, 25, and 30 minutes.

# Display table head
print("Minutes    Calories Burned")
print("--------------------------")

# Write for loop to perform the operations
for time in range(10, 31, 5):

    calories_burned = time * 3.9

    print(time, "       ", calories_burned)


