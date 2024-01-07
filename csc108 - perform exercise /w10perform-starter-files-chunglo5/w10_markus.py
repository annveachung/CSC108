"""Week 10 Perform - Part 2

This code is provided solely for the personal and private use of students 
taking the CSC108 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files provided for this exercise are:
Copyright (c) 2022 Mario Badr, Jennifer Campbell, Tom Fairgrieve, Paul Gries, 
Sadia Sharmin, and Jacqueline Smith.
"""

# file name: w10_markus.py
#
# Complete the following steps:
# (1) In addition to this file, download and open 
#     fluffy_functions.py in Wing101.
# (2) Review the test cases you chose for the all_fluffy function as part of 
#     the Choosing Test Cases exercise in the Week 9 Rehearse/lecture.
# (3) Implement the test cases you chose as test methods in the TestAllFluffy
#     class below. Make sure you save your file regularly.
# (4) Run your tests on the correct version of all_fluffy from the 
#     fluffy_functions.py file, where it is named all_fluffy_v0. We have
#     provided an import statement below to help you do that. Make sure your
#     tests all run and pass when the correct code is provided.
# (5) Run your tests on the buggy versions of all_fluffy from the 
#     fluffy_functions.py file. The simplest way to do that is to make the
#     first import statement that we have provided into a comment, and then
#     uncomment one of the import statements that follow.  To test a different
#     buggy version of all_fluffy, uncomment a different import statement.
# (6) When convinced that your tests are complete, submit your modified
#     w10_markus.py file to MarkUs. You can find instructions on submitting a
#     file to MarkUs in the Week *2* Perform -> Accessing Part 2 of the
#     Week 2 Perform (For Credit) on PCRS.
# (7) Verify you have submit the right file to MarkUs by downloading it again
#     and checking it is the one you meant to submit.
# (8) We have also provided a checker test for you to run in MarkUs. This week
#     the checker runs your tests on a correct version of the all_fluffy
#     function.  We will not be marking your style on this exercise, so there
#     will be no PyTA check. We will run additional tests with different
#     versions of buggy code when we mark your submission.

import pytest

# Uncomment ONE of the following statements, depending on which version
# of all_fluffy you wish to test.  Only add/delete the comment (#) symbol.
from fluffy_functions import all_fluffy_v0 as all_fluffy
# from fluffy_functions import all_fluffy_v1 as all_fluffy
#from fluffy_functions import all_fluffy_v2 as all_fluffy
# from fluffy_functions import all_fluffy_v3 as all_fluffy


def test_empty_string() -> None:
    """Test that the empty string is fluffy."""
    expected = True
    actual = all_fluffy('')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg


# Add your other test methods here
def test_only_first_letter_fluffy() -> None:
    """Test that the string is fluffy when only the first char is fluffy."""
    expected = False
    actual = all_fluffy('fond')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg
    

def test_only_last_letter_fluffy() -> None:
    """Test that the string is fluffy when only the last char is fluffy."""
    expected = False
    actual = all_fluffy('picky')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg
    
    
def test_only_some_fluffy_letter_used() -> None:
    """Test that the string is fluffy when only some of the fluffy letters 
    are used"""
    expected = True
    actual = all_fluffy('fly')
    msg = "Expected {}, but returned {}".format(expected, actual)
    assert actual is expected, msg


if __name__ == '__main__':
    pytest.main(['w10_markus.py'])
