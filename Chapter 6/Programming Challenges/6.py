# Write a program that asks the user to enter five test scores. The program
# should display a letter grade for each score and the average test score. Write
# the following functions in the program:
# • calc_average — This function should accept five test scores as arguments and
#   return the average of the scores.
# • determine_grade — This function should accept a test score as an argument and
#   return a letter grade for the score, based on the following grading scale:
#     Score        Letter Grade
#     90–100       A
#     80–89        B
#     70–79        C
#     60–69        D
#     Below 60     F

def main():
    
    # Prompt user for 5 test scores
    score_1 = float(input("Enter test score 1: "))
    score_2 = float(input("Enter test score 2: "))
    score_3 = float(input("Enter test score 3: "))
    score_4 = float(input("Enter test score 4: "))
    score_5 = float(input("Enter test score 5: "))

    display_scores(score_1, score_2, score_3, score_4, score_5)
    

# This function will accept 5 float arguments for test scores
# The function will calculate and return the average of those 5 scores
def calculate_average(score_1, score_2, score_3, score_4, score_5):

    average = (score_1 + score_2 + score_3 + score_4 + score_5) / 5

    return average

# This function will accept a float argument for score
# The scores letter grade will be determined and returned
# as a string
def determine_grade(score):

    if score < 60:
        letter_grade = "F"
    elif score >= 60 and score <= 69:
        letter_grade = "D"
    elif score >= 70 and score <= 79:
        letter_grade = "C"
    elif score >= 80 and score <= 89:
        letter_grade = "B"
    else:
        letter_grade = "A"

    return letter_grade

def display_scores(score_1, score_2, score_3, score_4, score_5):

    print("Test Score        Letter Grade")
    print("------------------------------")

    print(format(score_1,'3.0f'), determine_grade(score_1), sep = " " * 21 )
    print(format(score_2,'3.0f'), determine_grade(score_2), sep = " " * 21 )
    print(format(score_3,'3.0f'), determine_grade(score_3), sep = " " * 21 )
    print(format(score_4,'3.0f'), determine_grade(score_4), sep = " " * 21 )
    print(format(score_5,'3.0f'), determine_grade(score_5), sep = " " * 21 )

    print("\nAverage:", calculate_average(score_1, score_2, score_3, score_4, score_5))
        
main()
