"""
This function verified if a year is lead year or not.
"""

def leap_year(year):
    """
    A function that determines whether a given year is a leap year.

    param: year - int: The year that will be checked to determine if it is a leap year.
    return: True or False - boolean: return if the year is leap year or not.
    """

    if year < 0:
        raise ValueError("the year must be greater than zero")

    if year%4 != 0:
        return False
    if year%100 == 0 and year%400 != 0:
        return False
    return True
