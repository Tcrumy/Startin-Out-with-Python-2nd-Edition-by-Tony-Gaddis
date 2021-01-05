# Write a program that uses nested loops to collect data and calculate the
# average rainfall over a period of years. The program should first ask for the
# number of years. The outer loop will iterate once for each year. The inner
# loop will iterate twelve times, once for each month. Each iteration of the
# inner loop will ask the user for the inches of rainfall for that month. After
# all iterations, the program should display the number of months, the total
# inches of rainfall, and the average rainfall per month for the entire period.

# Prompt user for number of years
years = int(input("Enter how many years of data was collected: "))

# Define accumulator variable for rainfall total
total_rainfall = 0

# Calculate the number of months of data collected
months_of_data = 12 * years

# Write for loop to perform ranfall calculations
for year in range(years):
    
    for month in range(1,13):

        print("Enter rainfall data for year", year + 1, "month", month, ": ", end = "")
        rainfall_this_month = float(input())

        total_rainfall += rainfall_this_month

print(months_of_data, "Months of data have been collected.")
print("Total rainfall: ", total_rainfall)
print("Month Average:  ", total_rainfall / months_of_data)
        
