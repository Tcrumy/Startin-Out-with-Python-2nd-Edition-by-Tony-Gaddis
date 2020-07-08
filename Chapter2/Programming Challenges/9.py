# Write a program that converts Celsius temperatures to Fahrenheit temperatures.
# The formula is as follows:
# F = 1.8C + 32
# The program should ask the user to enter a temperature in Celsius, and then
# display the temperature converted to Fahrenheit.

# Prompt user for temperature in celcius
temp_in_celcius = float(input("Enter temperature in celcius: "))

# Convert the celcius tempereature to fahrenheit
temp_in_fahrenheit = 1.8 * temp_in_celcius + 32

# Display information to the user
print(temp_in_celcius, "Degrees celcius is", temp_in_fahrenheit, "dgrees fahrenheit.")
