# Assume the following statement has been executed:
# number = 1234567.456
# Write a Python statement that displays the value referenced by the number 
# variable formatted as 1,234,567.5

number = 1234567.456

# In order for the commas and sigle decimal precision the formatting requires 
# to be displayed,the second argument in the format function needs to be ',.1f'
print(format(number, ',.1f'))
