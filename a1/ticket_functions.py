"""CSC108: Fall 2023 -- Assignment 1: Airline Tickets

This code is provided solely for the personal and private use of students taking
CSC108 at the University of Toronto. Copying for purposes other than this use is
expressly prohibited. All forms of distribution of this code, whether as given 
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Sadia Sharmin, Jacqueline Smith, and Sophia Huynh.
"""

# Constants
YEAR = 0
MONTH = 4
DAY = 6
FROM = 8
TO = 11
SEAT = 14
FLYER = 17

WINDOW = 'window'
AISLE = 'aisle'
MIDDLE = 'middle'


def get_flyer_info(ticket: str) -> str:
    """Return the flyer number of the flyer for this ticket, if present. 
    Otherwise, return the empty string.
    
    >>> get_flyer_info('20230915YYZYEG12F')
    ''
    >>> get_flyer_info('20230915YYZYEG12F1236')
    '1236'
    """
    return ticket[FLYER:]


def visits_airport(ticket: str, airport: str) -> bool:
    """Return true if and only if airport is either the From or To airport on 
    this ticket. 
    Otherwise, return False.
    
    >>> visits_airport('20230915YYZYEG12F', 'YYZ')
    True
    >>> visits_airport('20230915YYZYEG12F1236', 'FLL')
    False
    """
    from_airport = ticket[FROM:TO]
    to_airport = ticket[TO:SEAT]
    return from_airport == airport or to_airport == airport


def get_seat_type(ticket: str) -> str:
    """Return 'window', 'aisle', or 'middle' depending on the seat type. 
    Otherwise, return the empty string.
    
    >>> get_seat_type('20230915YYZYEG12F')
    'window'
    >>> get_seat_type('20230915YYZYEG12P')
    ''
    """
    seat = ticket[SEAT + 2]
    if seat == 'A' or seat == 'F':
        return WINDOW
    elif seat == 'B' or seat == 'E':
        return MIDDLE
    elif seat == 'C' or seat == 'D':
        return AISLE 
    else:
        return ''


def is_valid_seat(ticket: str) -> bool:
    """Return return True if and only if the seat in this ticket is in a row 
    between 1 and 30, and has a seat letter A, B, C, D, E, or F. 
    Otherwise, return False.
    
    >>> is_valid_seat('20230915YYZYEG12F')
    True
    >>> is_valid_seat('20230915YYZYEG35A')
    False
    """
    seat_row = ticket[SEAT:SEAT + 2]
    seat_letter = ticket[SEAT + 2]
    return 1 <= int(seat_row) <= 30 and seat_letter in 'ABCDEF'
        
        
def is_valid_flyer(ticket: str) -> bool:
    """Return True if and only if a non-empty flyer number is valid or it is an 
    empty flyer number.
    A non-empty flyer number is valid if it consists of exactly four digits and 
    the sum of the first three digits taken modulo 10 is equal to the fourth 
    digit.
    Otherwise, return False.
    
    >>> is_valid_flyer('20230915YYZYEG12F')
    True
    >>> is_valid_flyer('20230915YYZYEG12F3882')
    False
    """
    flyer_num = ticket[FLYER:]
    
    if flyer_num == '':
        return True
    
    total = int(flyer_num[0]) + int(flyer_num[1]) + int(flyer_num[2])
    
    return (flyer_num.isdigit() and len(flyer_num) == 4 
            and int(flyer_num[3]) == total % 10)


def is_valid_ticket(ticket: str) -> bool:
    """Return True if and only if the ticket has a valid seat, a valid flyer 
    number, and has different From and To airports.
    Otherwise, return False.
    
    >>> is_valid_ticket('20230915YYZYEG12F')
    True
    >>> is_valid_ticket('20230915YYZYEG12F3882')
    False
    """
    diff_airport = ticket[FROM:TO] != ticket[TO:SEAT]
    return is_valid_seat(ticket) and is_valid_flyer(ticket) and diff_airport


def days_until(ticket: str, date: str) -> int:
    """Return return the number of days from date until the ticket date. The 
    number of days returned can be negative if the ticket date comes before the 
    given date.
    
    >>> days_until('20230915YYZYEG12F', '20230829')
    16
    >>> days_until('20240217YYZYEG12F1236', '20240301')
    -14
    """
    
    year_to_days = (int(ticket[YEAR:MONTH]) - int(date[YEAR:MONTH])) * 365
    month_to_days = (int(ticket[MONTH:DAY]) - int(date[MONTH:DAY])) * 30
    days = int(ticket[DAY:FROM]) - int(date[DAY:FROM])
    
    return year_to_days + month_to_days + days
