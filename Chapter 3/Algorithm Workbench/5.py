# Look at the following function definition:
# def my_function(a, b, c):
#     d = (a + c) / b
#     print(d)
# a. Write a statement that calls this function and uses keyword arguments 
# to pass 2 into a, 4 into b, and 6 into c.
# b. What value will be displayed when the function call executes?

# Define the function
def my_function(a, b, c):
    d = (a + c) / b
    print(d)

# Call the function using specified keyword arguments
# Output should be as follows:
# 2.0
my_function(a = 2, b = 4, c =6)
