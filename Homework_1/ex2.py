# Floris van Rossum
# CS4341 - Homework 1
# Professor Carlo Pinciroli
# Exercise 2
# ex2.py

def isreverse(s1, s2):
    """ Check if one string is the reverse of the other"""
    # Your code here

    # Check for two empty strings
    if s1 is "" and s2 is "":
        return True

    # If the lengths are not the same, they can't be the reverse of eachother!
    if len(s1) is not len(s2):
        return False

    # Call recursive function
    return rec_func(s1, s2, 0)

def rec_func(s1, s2, num):
    """Recursive function that checks two strings against each-other"""
    length = len(s1) - 1 # Determine the length of the string

    # Determine if the two characters are the same
    if s1[num] == s2[length - num]:
        # Characters are the same

        # Check if end of string is reached
        if num == length:
            # End of the string is reached, strings are reverse
            return True
        else:
            # End is not reached, call same function
            return rec_func(s1, s2, num + 1)
    else:
        # Characters are not the same
        return False
