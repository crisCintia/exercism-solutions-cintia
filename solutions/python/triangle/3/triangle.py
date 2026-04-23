"""
Functions to determine if a triangle is equilateral, isosceles, or scalene.

The instructions are:
- An equilateral triangle has all three sides of the same length.
- An isosceles triangle has at least two sides of the same length.
- A scalene triangle has all sides of different lengths.

And another function to check if the sides form a triangle using these equations:
- a + b >= c
- b + c >= a
- a + c >= b
"""

def is_triangle(sides):
    """
    Function to check if the sides form a triangle

    param: sides - list: the three sides of triangle
    return True or False - boolean: return if the sides form a triangle or not.
    """
    side_a_triangle, side_b_triangle, side_c_triangle = sides
    
    if side_a_triangle + side_b_triangle >= side_c_triangle and side_b_triangle + side_c_triangle >= side_a_triangle and side_a_triangle + side_c_triangle >= side_b_triangle and all(sides)>0:
        return True
    return False

def equilateral(sides):
    """
    Function to determinate if a triangle is equilateral

    param: sides - list: the three sides of triangle
    return True or False - boolean: return if is equilateral triangle or not.
    """
    if not is_triangle(sides):
        return False
        #raise ValueError("is not triangle")
    if len(set(sides)) == 1:
        return True
    return False


def isosceles(sides):
    """
    Function to determinate if a triangle is isosceles

    param: sides - list: the three sides of triangle
    return True or False - boolean: return if is isosceles triangle or not.
    """

    if not is_triangle(sides):
        return False
        #raise ValueError("is not triangle")
    if len(set(sides)) <= 2:
        return True
    return False


def scalene(sides):
    """
    Function to determinate if a triangle is scalene

    param: sides - list: the three sides of triangle
    return True or False - boolean: return if is scalene triangle or not.
    """
    if not is_triangle(sides):
        return False
        #raise ValueError("is not triangle")
    if len(set(sides)) == 3:
        return True
    return False
