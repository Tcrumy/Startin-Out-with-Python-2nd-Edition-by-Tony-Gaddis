# This exercise assumes you have already written the is_prime function in
# Programming Exercise 8. Write another program that displays all of the prime
# numbers from 1 through 100. The program should have a loop that calls the
# is_prime function.

def main():

    # Run the function for all numbers 1 - 100
    for number in range(101):
        if is_prime(number):
            print(number)
   

# This function will accept an integer argument
# The number will be tested to see if it is a prime
# number. If the number is prime, true will be
# returned, otherwise, false will be returned
def is_prime(num):

    # This if statement will handle any even numbers
    if num % 2 == 0:
        result = False

    # 1 is not a prime number, so we'll reject that too 
    elif num <= 1:
        result = False

    # 2 and 3 are both considered prime numbers and should be accepted   
    elif num == 2 or num == 3:
        result = True

    # This else will handle any number that has not previously been handled
    else:

        # It's computationally faster to start at the number 3,
        # our last handled number, and skip by two each step.
        # This will ensure that only odd numbers are checked
        # since only odd numbers can be prime
        for number in range(3, num, 2):

            if num % number == 0:
                result = False

                # If a number is found not to be prime
                # break out of the loop to prevent any
                # unneeded testing
                break

            else:
                result = True

    return result
            

main()

    

    
