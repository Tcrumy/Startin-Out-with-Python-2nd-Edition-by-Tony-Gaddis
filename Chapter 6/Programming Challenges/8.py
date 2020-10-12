# A prime number is a number that is only evenly divisible by itself and 1. For
# example, the number 5 is prime because it can only be evenly divided by 1 and
# 5. The number 6, however, is not prime because it can be divided evenly by 1,
# 2, 3, and 6. Write a Boolean function named is_prime which takes an integer as
# an argument and returns True if the argument is a prime number, or False other
# wise. Use the function in a program that prompts the user to enter a number
# and then displays a message indicating whether the number is prime.

def main():

    # Prompt user for a number
    number = int(input("Enter a number: "))

    # User the is_prime function to determine the
    # correct message to display to the user
    if is_prime(number):
        print(number, "Is a prime number")
    else:
        print(number, "Is not a prime number")

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

    

    
