"""Week 10 Perform - Part 2

Versions of all_fluffy to test your tests for Week 10 Perform Part 2.

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files provided for this exercise are:
Copyright (c) 2022 Mario Badr, Jennifer Campbell, Tom Fairgrieve, Paul Gries, 
Sadia Sharmin, and Jacqueline Smith.
"""

# Correct version
def all_fluffy_v0(s: str) -> bool:
    """Return True if and only if every letter in s is fluffy. 
    Fluffy letters are those that appear in the word 'fluffy'.

    >>> all_fluffy('fullfly')
    True
    >>> all_fluffy('firefly')
    False
    """

    for ch in s:
        if not ch in 'fluffy':
            return False
    return True


# Three buggy versions    
def all_fluffy_v1(s: str) -> bool:
    """Return True if and only if every letter in s is fluffy. 
    Fluffy letters are those that appear in the word 'fluffy'.
    """

    for ch in s:
        if ch in 'fluffy':
            return True
        else:
            return False


def all_fluffy_v2(s: str) -> bool:
    """Return True if and only if every letter in s is fluffy. 
    Fluffy letters are those that appear in the word 'fluffy'.
    """

    for ch in s:
        if ch in 'fluffy':
            result = True
        else:
            result = False

    return result


def all_fluffy_v3(s: str) -> bool:
    """Return True if and only if every letter in s is fluffy. 
    Fluffy letters are those that appear in the word 'fluffy'. 
    """

    result = True
    for ch in 'fluffy':
        if ch not in s:
            result = False

    return result
