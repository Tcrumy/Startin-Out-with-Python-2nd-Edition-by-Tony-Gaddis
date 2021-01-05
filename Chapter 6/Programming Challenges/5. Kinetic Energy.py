# In physics, an object that is in motion is said to have kinetic energy (KE).
# The following formula can be used to determine a moving object’s kinetic
# energy:
#     KE = 1⁄2 mv^2
# The variables in the formula are as follows: KE is the kinetic energy in
# joules, m is the object’s mass in kilograms, and v is the object’s velocity in
# meters per second. Write a function named kinetic_energy that accepts an
# object’s mass in kilograms and velocity in meters per second as arguments. The
# function should return the amount of kinetic energy that the object has. Write
# a program that asks the user to enter values for mass and velocity, and then
# calls the kinetic_energy function to get the object’s kinetic energy.

def main():

    # Prompt user for mass of object in kilograms and velocity of object
    mass = float(input("Enter objects mass in kilograms: "))
    velocity = float(input("Enter objects velocity: "))

    # Calculate the objects kinetic energy
    k_energy = kinetic_energy(mass, velocity)

    # Display information to the user
    print("The objects kinetic energy is", format(k_energy,".2f"), "joules.")




# This function will accept two numerical arguments, one for
# mass in kilograms, one for the velocity the mass is moving
# The kinetic energy of the object will be returned.
def kinetic_energy(mass, velocity):

    return .5 * mass * velocity**2

main()
