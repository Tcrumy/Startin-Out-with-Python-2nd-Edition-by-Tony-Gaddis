# The Springfork Amateur Golf Club has a tournament every weekend. The club
# president has asked you to write two programs:
# 1. A program that will read each player’s name and golf score as keyboard
# input, and then save these as records in a file named golf.txt.
# (Each record will have a field for the player’s name and a field for the
# player’s score.)
# 2. A program that reads the records from the golf.txt file and displays them.

# This will be program 10-2

def main():

    outfile = open("golf.txt","r")

    players_name = outfile.readline()
    players_score = outfile.readline()


    while players_name != "":
        print("Player: ", players_name, end="")
        print("Score: ", players_score)
        
        players_name = outfile.readline()
        players_score = outfile.readline()

        
main()
        
