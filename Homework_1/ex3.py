# Floris van Rossum
# CS4341 - Homework 1
# Professor Carlo Pinciroli
# Exercise 3
# ex3.py

import re

def wordset(fname):
    """Returns the set of words corresponding to the given file"""
    # Create regexp for character filtering
    regex = re.compile('[^a-zA-Z ]')

    # Your code here

    # Open the file
    file = open(fname, mode='r')
    file_string = file.read()

    # Filter out the regex
    modified_string = regex.sub(' ', file_string)

    # Set to lowercase
    lowered_string = modified_string.lower()

    # Split into individual words and return
    return lowered_string.split()

def jaccard(fname1, fname2):
    """Calculate Jaccard index"""
    # Your code here - call wordset()
    file_string1 = wordset(fname1)
    file_string2 = wordset(fname2)

    # Calculate the intersection of words
    intersection_arr = intersection(file_string1, file_string2)

    # Calculate the union of words
    union_arr = union(file_string1, file_string2)

    # Calculate the jaccard index
    jaccard_index = len(intersection_arr) / len(union_arr)

    # print("\n\nJACCARD INDEX: " + str(jaccard_index))
    return jaccard_index

def intersection(words1, words2):
    """Calculate the intersection between two word sets"""
    return_arr = [] # Array of intersection words

    # Filter through all the words to determine which are in both arrays
    for word in words1:

        for word2 in words2:

            if word2 == word:

                # Check if the word is already in the array
                contained = False

                for match_word in return_arr:

                    if match_word == word:
                        contained = True
                        # word is already in the array, break!
                        break

                if not contained:
                    # Word is not in the array, so add it
                    return_arr.append(word)

    # print("Intersection arr: " + str(return_arr))
    return return_arr

def union(words1, words2):
    """Calculate the union between two wordsets"""
    return_arr = []

    # Add all the words from the first array
    for word in words1:

        contained = False  # Contain boolean

        # Check if word is already in the array
        for word1 in return_arr:

            if word1 == word:
                contained = True

        if not contained:
            return_arr.append(word)

    # Add all the words from the second array if they are not yet in the array
    for word in words2:

        contained = False # Contain boolean

        # Check if word is already in the array
        for word1 in return_arr:

            if word1 == word:
                contained = True

        if not contained:
            return_arr.append(word)

    # print("Union arr: " + str(return_arr))
    return return_arr

jaccard("alice.txt", "glass.txt")