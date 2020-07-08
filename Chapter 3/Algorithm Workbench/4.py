# What will the following program display?
# def main():
#   x = 1
#   y = 3.4
#   print(x, y)
#   change_us(x, y)
#   print(x, y)
# def change_us(a, b):
#   a = 0
#   b = 0
#   print(a, b)
# main()


# The display should be as follows
# 1 3.4
# 0 0
# 1 3.4
# The reason a and b are not 0 in the final print statement is that the
# change_us(x,y) function only changes a copy of the x and y variables
# This change has not affect on x or y outside of the change_us function
def main():
    x = 1
    y = 3.4
    print(x, y)
    change_us(x, y)
    print(x, y)
def change_us(a, b):
    a = 0
    b = 0
    print(a, b)

main()
