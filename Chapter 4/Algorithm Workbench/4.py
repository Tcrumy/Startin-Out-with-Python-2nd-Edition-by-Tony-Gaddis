# The following code contains several nested if-else statements. Unfortunately,
# it was written without proper alignment and indentation. Rewrite the code and
# the proper conventions of alignment and indentation.


# Without proper alignment and indentation
"""
if score >= A_SCORE:
print('Your grade is A.')
else:
if score >= B_SCORE:
print('Your grade is B.')
else:
if score >= C_SCORE:
print('Your grade is C.')
else:
if score >= D_SCORE:
print('Your grade is D.')
else:
print('Your grade is F.')
"""


# With proper alignment and indentation
if score >= A_SCORE:
    print('Your grade is A.')
else:
    if score >= B_SCORE:
        print('Your grade is B.')

    else:
        if score >= C_SCORE:
            print('Your grade is C.')

        else:
            if score >= D_SCORE:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
