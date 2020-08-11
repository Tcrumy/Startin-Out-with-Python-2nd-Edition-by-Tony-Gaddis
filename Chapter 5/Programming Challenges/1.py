# A bug collector collects bugs every day for seven days. Write a program that
# keeps a running total of the number of bugs collected during the seven days.
# The loop should ask for the number of bugs collected for each day, and when
# the loop is finished, the program should display the total number of bugs
# collected.

# Setup loop control variable for number of iterations
DAYS = 7

# Define a variable to hold number of bugs collected
bugs_collected = 0

# Write for loop to ask for number of bugs collected on each day
for day in range(DAYS):

    print("Enter bugs collected on day", day + 1, ": ", end = "")
    collected_this_day = int(input(""))

    bugs_collected += collected_this_day

print("Total number of bugs collected:", bugs_collected)

    
    
