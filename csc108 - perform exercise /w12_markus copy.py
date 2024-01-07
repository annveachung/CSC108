"""Week 12 Perform - Part 2

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files provided for this exercise are:
Copyright (c) 2021 Mario Badr, Jennifer Campbell, Tom Fairgrieve, Paul Gries,
Sadia Sharmin, and Jacqueline Smith.


Complete the following steps:

(1) The starter code below contains the instructions for three past exam
    questions. Each function has a docstring provided, and you will write the
    body. The past exam the question is taken from is indicated in a comment.
(2) Test your functions in the Wing101 shell by evaluating the examples from
    the docstrings and confirming that the correct result is displayed. You can
    also uncomment doctest.testmod() to try running the docstring examples for
    a quicker way to test.
(3) When convinced that your functions are correct, submit your modified file
    to MarkUs. You can find instructions on submitting a file to MarkUs
    in the Week *2* Perform on PCRS.
(4) We have also provided a checker for you to run in MarkUs. * NOTE: Unlike in
    the previous Performs, we are providing you with the full set of tests so
    that you will be able to use them to check your work. This also means you
    will know if you earned full marks or not.
"""

from typing import TextIO


# Winter 2017 Q4a
def separate_and_reverse_vowels(s: str) -> list[str]:
    """Return a list containing two strings made up from the characters in s.
    The first string contains all of the characters in s that are vowels (a,
    A, e, E, i, I, o, O, u, or U) in an order that is OPPOSITE to how they
    appear in s.
​
    The second string contains all of the other characters from s (the
    characters that are not vowels) in the SAME order as they appear in s.
​
    >>> separate_and_reverse_vowels('Catherine wants to go to the ZOO.')
    ['OOeoooaeiea', 'Cthrn wnts t g t th Z.']
    >>> separate_and_reverse_vowels('108!!!')
    ['', '108!!!']
    """
    
    # TODO complete the body of this function
    result = []
    vowel = ''
    consonant = ''
    for i in range(len(s) -1, -1, -1):
        if s[i] in 'aAeEiIoOuU':
            vowel = vowel + s[i]
    for char in s:
        if char not in 'aAeEiIoOuU':
            consonant = consonant + char
    result.append(vowel)
    result.append(consonant)
    return result 


# Fall 2017 Q11a
"""Station data is stored in a comma separated values (CSV) file with one
station's ID, name, latitude, and longitude per line in that order.  Here is an 
example station data CSV file:

1,Allen,43.667158,-79.4028
12,Bayview,43.656518,-79.389
8,Chester,43.648093,-79.384749
17,Davisville,43.66009,-79.385653

Given the example station data CSV file open for reading, function 
build_dictionaries returns:

({1: [43.667158, -79.4028], 12: [43.656518, -79.389],
  8: [43.648093, -79.384749], 17: [43.66009, -79.385653]},
 {1: 'Allen', 12: 'Bayview', 8: 'Chester', 17: 'Davisville'})

Complete the function build_dictionaries according to the example above and its
docstring below. Assume the given file has the correct format.
"""


def build_dictionaries(f: TextIO
                       ) -> tuple[dict[int, list[float]], dict[int, str]]:
    """Return a tuple of two dictionaries with station data from f.
    The first dictionary has station IDs as keys and station locations (two item
    lists with latitude and longitude) as values.
    The second dictionary has station IDs as keys and station names as values.

    Precondition: station IDs in f are unique
    """
    
    # TODO complete the body of this function
    dict_1 = {}
    dict_2 = {}
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        [id, name, lat, long] = line.split(',')
        dict_1[int(id)] = [float(lat), float(long)]
        dict_2[int(id)] = name
    return (dict_1, dict_2)


# Fall 2018 Q8
"""Complete the function below to according to its docstring.

To receive full marks on this function, your solution must not remove any keys 
from the parameter totals, even temporarily, such as by using the method 
dict.clear()
"""


def update_amounts(totals: dict[str, int], amts: list[tuple[str, int]]) -> None:
    """Update the relevant values in the totals dictionary by the new amounts
    from each tuple given in amts.

    The first element in each tuple in amts represents the key in the
    totals dictionary whose value must be updated by the second element
    in that tuple.

    If no such key exists, a new key-value pair with the tuple's elements
    are added to the totals dictionary.

    >>> D = {}
    >>> update_amounts(D, [('visa', 1000), ('amex', 50), ('visa', 500)])
    >>> D
    {'visa': 1500, 'amex': 50}
    >>> update_amounts(D, [('amex', 50), ('visa', 1000), ('mc', 100)])
    >>> D
    {'visa': 2500, 'amex': 100, 'mc': 100}
    >>> update_amounts(D, [('paypal', 25), ('amex', -100)])
    >>> D
    {'visa': 2500, 'amex': 0, 'mc': 100, 'paypal': 25}
    """
    
    # TODO complete the body of this function
    for item in amts:
        if item[0] in totals:
            totals[item[0]] += item[1]
        else:
            totals[item[0]] = item[1]


if __name__ == '__main__':
    import doctest
    #doctest.testmod()
