"""CSC108: Fall 2023 -- Assignment 3: arxiv.org

This code is provided solely for the personal and private use of students taking
CSC108 at the University of Toronto. Copying for purposes other than this use is
expressly prohibited. All forms of distribution of this code, whether as given 
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Anya Tafliovich, Michelle Craig, Tom Fairgrieve, Sadia
Sharmin, and Jacqueline Smith.
"""

import copy  # needed in examples of functions that modify input dict
from typing import TextIO

from constants import (ID, TITLE, CREATED, MODIFIED, AUTHORS, ABSTRACT, END,
                       NameType, ArticleValueType, ArticleType, ArxivType)


################################################################################
# Sample data for use in docstring examples
################################################################################
EXAMPLE_ARXIV = {
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
        ABSTRACT: 'We present clear evidence that Introduction to\n'
        + 'Computer Programming is the best course'},
    '42': {
        ID: '42',
        TITLE: '',
        CREATED: '2023-05-04',
        MODIFIED: '2023-05-05',
        AUTHORS: [],
        ABSTRACT: 'This is a strange article with no title\n'
        + 'and no authors.\n\nIt also has a blank line in its abstract!'}
}

EXAMPLE_BY_AUTHOR = {
    ('Campbell', 'Jen'): ['108'],
    ('Grossman', 'Tovi'): ['03221'],
    ('Sharmin', 'Sadia'): ['0001'],
    ('Smith', 'Jacqueline E.'): ['0001', '108'],
    ('Yanez', 'Fernando'): ['5090'],
    ('Zavaleta-Bernuy', 'Angela'): ['108', '5090']
}


################################################################################
# Helper function to use in your code later on.  Do not change these functions.
################################################################################
def clean_word(word: str) -> str:
    """Return word with all non-alphabetic characters removed and converted to 
    lowercase.
    
    Precondition: word contains no whitespace
    
    >>> clean_word('Hello!!!')
    'hello'
    >>> clean_word('12cat.dog?')
    'catdog'
    >>> clean_word("DON'T")
    'dont'
    """
    
    new_word = ''
    for ch in word:
        if ch.isalpha():
            new_word = new_word + ch.lower()
    return new_word


################################################################################
# Task 1 - Working with ArxivType
################################################################################
# TODO write your functions for Task 1 here
def created_in_year(data: ArxivType, id: str, year: int) -> bool:
    """Return true if and only if the string id occurs in the ArxivType data 
    and was published in the given integer year.
    
    >>> created_in_year(EXAMPLE_ARXIV, '03221', 2023)
    True
    >>> created_in_year(EXAMPLE_ARXIV, '5090', 2023)
    False
    """
    
    if id in data and data[id][CREATED] != "":
        return int(data[id][CREATED][0:4]) == year
    return False


def contains_keyword(data: ArxivType, keyword: str) -> list[str]:
    """Return a list of strings of the IDs of articles from the ArxivType data 
    that contain the string keyword in their title, author names, and/or 
    abstract. 
    
    >>> contains_keyword(EXAMPLE_ARXIV, "angela")
    ['108', '5090']
    >>> contains_keyword(EXAMPLE_ARXIV, "cat")
    []
    """
    
    result = []
    for item in data:
        title_words = data[item][TITLE].split(" ")
        
        author_words = []
        for author in data[item][AUTHORS]:
            for name in author:
                author_words = author_words + name.split(" ")
                
        abstract_words = data[item][ABSTRACT].split(" ")
        
        words = title_words + author_words + abstract_words
        
        found = False
        for word in words:
            if clean_word(word) == keyword:
                found = True
                break
        if found:
            result.append(item)
            
    result.sort()
    return result


def average_author_count(data: ArxivType) -> float:
    """Return the average number of authors per article in the ArxivType data.
    
    >>> average_author_count(EXAMPLE_ARXIV)
    1.6
    >>> average_author_count({})
    0.0
    """
    
    if len(data) == 0:
        return 0.0

    count = 0 
    for item in data:
        count = count + len(data[item][AUTHORS])
    return count / len(data)
    
    
################################################################################
# Task 2 - Reading in the arxiv metadata
################################################################################
def read_arxiv_file(f: TextIO) -> ArxivType:
    """Return a ArxivType dictionary containing the arxiv metadata in f.

    Note we do not include example calls for functions that take open files.
    """

    # TODO write the body of the function here
    arxiv = ArxivType()
    
    line = f.readline()
    while line != "":
        id = line.strip()
        title = f.readline().strip()
        created = f.readline().strip()
        modified = f.readline().strip()
        
        line = f.readline().strip()
        authors = []
        while line != "":
            author = NameType(tuple(line.split(",")))
            authors.append(author)
            line = f.readline().strip()
        
        line = f.readline().strip()
        abstract_lines = []    
        while line != END:
            abstract_lines.append(line)
            line = f.readline().strip()    
        abstract = "\n".join(abstract_lines)

        article = ArticleType()        
        article[ID] = id
        article[TITLE] = title
        article[CREATED] = created
        article[MODIFIED] = modified
        article[AUTHORS] = authors
        article[ABSTRACT] = abstract
        arxiv[id] = article
        
        line = f.readline()
        
    return arxiv
    
    
# TODO write any helper functions you need for Task 2 here

################################################################################
# Task 3 - Working with Authors and Coauthors
################################################################################
def make_author_to_articles(id_to_article: ArxivType
                            ) -> dict[NameType, list[str]]:
    """Return a dictionary that maps each author name to a list (sorted in
    lexicographic order) of IDs of articles written by that author,
    based on the information in the ArxivType id_to_article.

    >>> make_author_to_articles(EXAMPLE_ARXIV) == EXAMPLE_BY_AUTHOR
    True
    >>> make_author_to_articles({})
    {}
    """
    # We have provided the docstring for this function as an example of how
    # to compare dictionaries in a docstring example
    
    # TODO write the body of the function here
    result = {}
    for item in id_to_article:
        for author in id_to_article[item][AUTHORS]:
            if author not in result:
                result[author] = []
            result[author].append(item)
    for author in result:
        result[author].sort()
    return result


# TODO write the rest of your Task 3 functions here
def get_coauthors(data: ArxivType, author: NameType
                            ) -> list[NameType]:
    """Return a list of coauthors of the author specified by 
    the NameType author (sorted in lexicographic order).

    >>> get_coauthors(EXAMPLE_ARXIV, ('Smith', 'Jacqueline E.'))
    [('Campbell', 'Jen'), ('Sharmin', 'Sadia'), ('Zavaleta-Bernuy', 'Angela')]
    >>> get_coauthors(EXAMPLE_ARXIV, ('Grossman', 'Tovi'))
    []
    """
    
    result = []
    for item in data:
        if author in data[item][AUTHORS] and len(data[item][AUTHORS]) > 1:
            for coauthor in data[item][AUTHORS]:
                result.append(coauthor)
            result.remove(author)
    result.sort()
    return result


def get_most_published_authors(data: ArxivType) -> list[NameType]:
    """Return a list of NameType authors with the most published 
    articles (sorted in lexicographic order) based on the ArxivType data.

    >>> get_most_published_authors(EXAMPLE_ARXIV)
    [('Smith', 'Jacqueline E.'), ('Zavaleta-Bernuy', 'Angela')]
    >>> get_most_published_authors({})
    []
    """
    
    author_to_article = make_author_to_articles(data)
    result = []
    greatest = 0
    for author in author_to_article:
        if len(author_to_article[author]) >= greatest:
            greatest = len(author_to_article[author])
    for author in author_to_article:
        if len(author_to_article[author]) == greatest:
            result.append(author)
    result.sort()
    return result


def suggest_collaborators(data: ArxivType, author: NameType) -> list[NameType]:
    """Return a list of Nametype authors with whom NameType author specified is 
    encouraged to collaborate (sorted in lexicographic order), given the 
    ArxivType data.

    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Yanez', 'Fernando'))
    [('Campbell', 'Jen'), ('Smith', 'Jacqueline E.')]
    >>> suggest_collaborators(EXAMPLE_ARXIV, ('Grossman', 'Tovi'))
    []
    """
    
    direct_coauthors = get_coauthors(data, author) 
    all_author = []
    result = []
    for coauthor in direct_coauthors:
        indirect_coauthors = get_coauthors(data, coauthor) 
        for indirect_coauthor in indirect_coauthors:
            all_author.append(indirect_coauthor)
    for current_author in all_author:
        if current_author not in result:
            result.append(current_author)
    if author in result:
        result.remove(author)
    result.sort()
    return result
    
    
################################################################################
# Task 4 - Prolific Authors
################################################################################
def keep_prolific_authors(id_to_article: ArxivType,
                          min_publications: int) -> None:
    """Update id_to_article so that it contains only articles published by
    authors with min_publications or more articles published. As long
    as at least one of the authors has min_publications, the article
    is kept.

    >>> arxiv_copy = copy.deepcopy(EXAMPLE_ARXIV)
    >>> keep_prolific_authors(arxiv_copy, 2)
    >>> len(arxiv_copy)
    3
    """
    # We have provided you with this docstring as an example of how to use 
    # the function copy.deepcopy in docstring examples for functions that
    # modify an argument.

    # TODO write the body of the function here

    author_to_articles = make_author_to_articles(id_to_article)
    remove_list = []
    for id in id_to_article:
        if not has_prolific_authors(author_to_articles, id_to_article[id], 
                                min_publications):
            remove_list.append(id)
    for id in remove_list:
        id_to_article.pop(id)


# TODO write the rest of your Task 4 functions here
def has_prolific_authors(author_to_id: dict[NameType, 
                         list[str]], article: ArticleType, 
                         min_publications:int) -> bool:
    """Return True if and only if the ArticleType id has at least one author 
    who is considered prolific.

    >>> has_prolific_authors(EXAMPLE_BY_AUTHOR, EXAMPLE_ARXIV['5090'], 2)
    True
    >>> has_prolific_authors(EXAMPLE_BY_AUTHOR, EXAMPLE_ARXIV['03221'], 2)
    False
    """
    
    for target_author in article[AUTHORS]:
        if len(author_to_id[target_author]) >= min_publications:
            return True
    return False
            
            
if __name__ == '__main__':
    pass
    # uncomment the lines below to run doctest on your code
    # note that doctest requires your docstring examples to be perfectly
    # formatted, and we will not be running doctest on your code
    # import doctest
    # doctest.testmod()

    # uncomment the lines below to work with the small data set
    #example_data = open('example_data.txt')
    #example_arxiv = read_arxiv_file(example_data)
    #example_data.close()
    #if example_arxiv == EXAMPLE_ARXIV:
        #print('The result from your read_arxiv_file matches EXAMPLE_ARXIV!')
        #print('This is a good sign, but do more of your own testing!')
    #else:
        #print('Not quite! You got')
        #print(example_arxiv)
        #print()
        #print('If you are getting this message, then the dictionary produced')
        #print('by your read_arxiv_file function does not match the provided')
        #print('EXAMPLE_ARXIV. Scroll up to see the dictionary your function')
        #print('produced. You should write additional testing code to help')
        #print('figure out why it does not match. You can also try setting a')
        #print('breakpoint on the first line of read_arxiv_file and running')
        #print('the debugger.')

    # uncomment the lines below to work with a larger data set
    #data = open('data.txt')
    #arxiv = read_arxiv_file(data)
    #data.close()

    #author_to_articles = make_author_to_articles(arxiv)
    #most_published = get_most_published_authors(arxiv)
    #print(most_published)
    #print(get_coauthors(arxiv, ('Varanasi', 'Mahesh K.')))  # one
    #print(get_coauthors(arxiv, ('Chablat', 'Damien')))  # many
