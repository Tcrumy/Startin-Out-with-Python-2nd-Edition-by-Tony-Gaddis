# Serendipity Booksellers has a book club that awards points to its customers
# based on the number of books purchased each month. The points are awarded as
# follows:
#   • If a customer purchases 0 books, he or she earns 0 points.
#   • If a customer purchases 1 book, he or she earns 5 points.
#   • If a customer purchases 2 books, he or she earns 15 points.
#   • If a customer purchases 3 books, he or she earns 30 points.
#   • If a customer purchases 4 or more books, he or she earns 60 points.
# Write a program that asks the user to enter the number of books that he or she
# has purchased this month and displays the number of points awarded.

# Prompt the user to enter the number of books
# they've purchased this month
books_purchased = int(input("Enter the number of books purchased this month: "))

# Use if-elif-else decision structure to apply the correct
# number of points to the use
if books_purchased >= 4:
    points = 60
elif books_purchased == 3:
    points = 30
elif books_purchased == 2:
    points = 15
elif books_purchased == 1:
    points = 5
else:
    points = 0

# Display message to user
print("You have earned", points, "points this month.")
