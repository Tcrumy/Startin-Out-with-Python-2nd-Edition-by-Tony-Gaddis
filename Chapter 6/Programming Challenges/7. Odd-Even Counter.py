# In this chapter you saw an example of how to write an algorithm that
# determines whether a number is even or odd. Write a program that generates 100
# random numbers, and keeps a count of how many of those random numbers are even
# and how many are odd.

import random

def main():

    even_numbers = 0
    odd_numbers = 0

    number_count = 0

    while number_count < 100:
        random_number = random.randint(1,1000000)

        if random_number % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1

        number_count += 1


    print("Even: ", even_numbers)
    print("Odd : ", odd_numbers)

main()
