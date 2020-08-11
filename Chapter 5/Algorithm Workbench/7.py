# Write a set of nested loops that display 10 rows of # characters. There should
# be 15 # characters in each row.

for row in range(10):
    for column in range(15):
        print("#", end = "")
    print()
