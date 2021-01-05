# The Springfork Amateur Golf Club has a tournament every weekend. The club
# president has asked you to write two programs:
# 1. A program that will read each player’s name and golf score as keyboard
# input, and then save these as records in a file named golf.txt.
# (Each record will have a field for the player’s name and a field for the
# player’s score.)
# 2. A program that reads the records from the golf.txt file and displays them.

# This will be program 10-1

def main():

    infile = open("golf.txt","w")

    qty_of_players = int(input("How many players scores must be entered: "))

    for player in range(qty_of_players):

        players_name = input("Enter Players Name: ")
        players_score = input("Enter Players Score: ")

        infile.write(players_name + "\n")
        infile.write(players_score + "\n")

main()
