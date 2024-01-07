"""CSC108: Fall 2023 -- Assignment 3: arxiv.org

This code is provided solely for the personal and private use of students taking
CSC108 at the University of Toronto. Copying for purposes other than this use is
expressly prohibited. All forms of distribution of this code, whether as given 
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Anya Tafliovich, Michelle Craig, Tom Fairgrieve, Sadia
Sharmin, and Jacqueline Smith.
"""

import pytest
import arxiv_functions
from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS,
                       ABSTRACT, END, NameType, ArticleValueType,
                       ArticleType, ArxivType)


# You can use this sample dictionary in your tests, if you choose
# You can also create your own sample dictionaries 
TEST_ARXIV = {
    '5090': {
        ID: '5090',
        TITLE: "Increasing Students' Engagement to Reminder Emails",
        CREATED: '',
        MODIFIED: '2022-08-02',
        AUTHORS: [('Yanez', 'Fernando'), ('Zavaleta-Bernuy', 'Angela')],
        ABSTRACT: 'Our metric of interest is open email rates.'},
    '03221': {
        ID: '03221',
        TITLE: 'Stargazer: An Interactive Camera Robot for How-To Videos',
        CREATED: '2023-03-01',
        MODIFIED: '2023-03-06',
        AUTHORS: [('Grossman', 'Tovi')],
        ABSTRACT: ('We present Stargazer, a novel approach for assisting ' +
                   'with tutorial content creation.')},
    '0001': {
        ID: '0001',
        TITLE: 'Cats and Dogs Can Co-Exist',
        CREATED: '2023-08-20',
        MODIFIED: '2023-10-02',
        AUTHORS: [('Smith', 'Jacqueline E.'), ('Sharmin', 'Sadia')],
        ABSTRACT: 'We show a formal proof that cats and dogs\n' +
        'can peacefully co-exist!'},
    '108': {
        ID: '108',
        TITLE: 'CSC108 is the Best Course Ever',
        CREATED: '2023-09-01',
        MODIFIED: '',
        AUTHORS: [('Smith', 'Jacqueline E.'), ('Zavaleta-Bernuy', 'Angela'), 
                  ('Campbell', 'Jen')],
        ABSTRACT: 'We present clear evidence that Introduction to\n' + \
        'Computer Programming is the best course'},    
    '42': {
        ID: '42',
        TITLE: '',
        CREATED: '2023-05-04',
        MODIFIED: '2023-05-05',
        AUTHORS: [],
        ABSTRACT: 'This is a strange article with no title\n' + \
        'and no authors.\n\nIt also has a blank line in its abstract!'}
}

TEST_ARXIV_NO_AUTHORS = {
    '5090': {
        ID: '5090',
        TITLE: "Increasing Students' Engagement to Reminder Emails",
        CREATED: '',
        MODIFIED: '2022-08-02',
        AUTHORS: [],
        ABSTRACT: 'Our metric of interest is open email rates.'},
    '03221': {
        ID: '03221',
        TITLE: 'Stargazer: An Interactive Camera Robot for How-To Videos',
        CREATED: '2023-03-01',
        MODIFIED: '2023-03-06',
        AUTHORS: [],
        ABSTRACT: ('We present Stargazer, a novel approach for assisting ' +
                   'with tutorial content creation.')},
    '0001': {
        ID: '0001',
        TITLE: 'Cats and Dogs Can Co-Exist',
        CREATED: '2023-08-20',
        MODIFIED: '2023-10-02',
        AUTHORS: [],
        ABSTRACT: 'We show a formal proof that cats and dogs\n' +
        'can peacefully co-exist!'},
    '108': {
        ID: '108',
        TITLE: 'CSC108 is the Best Course Ever',
        CREATED: '2023-09-01',
        MODIFIED: '',
        AUTHORS: [],
        ABSTRACT: 'We present clear evidence that Introduction to\n' + \
        'Computer Programming is the best course'},    
    '42': {
        ID: '42',
        TITLE: '',
        CREATED: '2023-05-04',
        MODIFIED: '2023-05-05',
        AUTHORS: [],
        ABSTRACT: 'This is a strange article with no title\n' + \
        'and no authors.\n\nIt also has a blank line in its abstract!'}
}

TEST_ARXIV_ONE_AUTHOR_EACH = {
    '5090': {
        ID: '5090',
        TITLE: "Increasing Students' Engagement to Reminder Emails",
        CREATED: '',
        MODIFIED: '2022-08-02',
        AUTHORS: [('Yanez', 'Fernando')],
        ABSTRACT: 'Our metric of interest is open email rates.'},
    '03221': {
        ID: '03221',
        TITLE: 'Stargazer: An Interactive Camera Robot for How-To Videos',
        CREATED: '2023-03-01',
        MODIFIED: '2023-03-06',
        AUTHORS: [('Grossman', 'Tovi')],
        ABSTRACT: ('We present Stargazer, a novel approach for assisting ' +
                   'with tutorial content creation.')},
    '0001': {
        ID: '0001',
        TITLE: 'Cats and Dogs Can Co-Exist',
        CREATED: '2023-08-20',
        MODIFIED: '2023-10-02',
        AUTHORS: [('Smith', 'Jacqueline E.')],
        ABSTRACT: 'We show a formal proof that cats and dogs\n' +
        'can peacefully co-exist!'},
    '108': {
        ID: '108',
        TITLE: 'CSC108 is the Best Course Ever',
        CREATED: '2023-09-01',
        MODIFIED: '',
        AUTHORS: [('Zavaleta-Bernuy', 'Angela')],
        ABSTRACT: 'We present clear evidence that Introduction to\n' + \
        'Computer Programming is the best course'},    
    '42': {
        ID: '42',
        TITLE: '',
        CREATED: '2023-05-04',
        MODIFIED: '2023-05-05',
        AUTHORS: [('Campbell', 'Jen')],
        ABSTRACT: 'This is a strange article with no title\n' + \
        'and no authors.\n\nIt also has a blank line in its abstract!'}
}

TEST_ARXIV_TWO_ARTICLES_ONE_AUTHOR = {
    '5090': {
        ID: '5090',
        TITLE: "Increasing Students' Engagement to Reminder Emails",
        CREATED: '',
        MODIFIED: '2022-08-02',
        AUTHORS: [('Yanez', 'Fernando')],
        ABSTRACT: 'Our metric of interest is open email rates.'},
    '03221': {
        ID: '03221',
        TITLE: 'Stargazer: An Interactive Camera Robot for How-To Videos',
        CREATED: '2023-03-01',
        MODIFIED: '2023-03-06',
        AUTHORS: [],
        ABSTRACT: ('We present Stargazer, a novel approach for assisting ' +
                   'with tutorial content creation.')}
}

# TODO: Write your test functions here
# You can find an example of a pytest function in test_created_in_year.py
def test_empty_arxiv() -> None:
    """Test average_author_count with an empty arxiv.
    """
    
    actual = arxiv_functions.average_author_count(ArxivType({}))
    expected = 0.0
    assert actual == expected


def test_arxiv_no_author() -> None:
    """Test average_author_count with an arxiv with no authors in every article.
    """
    
    actual = arxiv_functions.average_author_count(TEST_ARXIV_NO_AUTHORS)
    expected = 0.0
    assert actual == expected


def test_arxiv_one_author() -> None:
    """Test average_author_count with an arxiv with one author in every article.
    """
    
    actual = arxiv_functions.average_author_count(TEST_ARXIV_ONE_AUTHOR_EACH)
    expected = 1
    assert actual == expected


def test_arxiv_two_articles_one_author() -> None:
    """Test average_author_count with an arxiv with 2 articles, with one having 
    one author and another one having no author.
    """
    
    actual = arxiv_functions.average_author_count(
        TEST_ARXIV_TWO_ARTICLES_ONE_AUTHOR)
    expected = 0.5
    assert actual == expected
    

if __name__ == '__main__':
    pytest.main(['test_average_author_count.py'])
