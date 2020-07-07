# Assume the variables result, w, x, y, and z are all integers, and that w = 5,
# x = 4, y = 8, and z = 2. What value will be stored in result after each of
# the following statements executes.
# a. result = x + y
# b. result = z * 2
# c. result = y / z
# d. result = y - z
# e. result = w // z

# NOTE: First lets assign all variables
result = 0
w = 5
x = 4
y = 8
z = 2

# Now lets perform an analyze each operation to see what result should be

# a. result = x + y, result = 4 + 8, result = 12
result = x + y
print(result)
# b. result = z * 2, result = 2 * 2, result = 4
result = z * 2
print(result)

# NOTE: division always returns a float answer. So, even though you may write
# the result of 8/2 as 4, 4.0 is what this operation will return
# c. result = y / z, result = 8 / 2, result = 4.0
result = y / z
print(result)

# d. result = y - z, result = 8 - 2, result = 6
result = y - z
print(result)

# NOTE: // means integer division. This will result in a whole number answer
# with no fractional part.
# e. result = w // z, result = 5 // 2, result = 2.
result = w // z
print(result)
