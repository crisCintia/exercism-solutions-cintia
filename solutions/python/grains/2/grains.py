# Define the constants
FIRST_SQUARE_OF_CHESS = 1 # This number represents the quantity of grains in the first square.
GROWTH_RATE = 2 # This number represents the number of grains doubles with each subsequent square.
TOTAL_NUMBER_OF_CHESS_SQUARES = 64 # A chessboard has 64 squares.

"""
The first function calculates the number of grains in a given square of the chessboard.
"""
def square(number):
    """
    Function to calculate the number of grains of wheat in a given square on a chessboard.

    param: number - int: This number represents the square of a specific square on a chessboard and         must be between 1 and 64.
    return number_grain_square - int: the number of grains on a given square
    """
    
    if number<1 or number>64:
        raise ValueError('square must be between 1 and 64')

    number_grain_square = FIRST_SQUARE_OF_CHESS * GROWTH_RATE**(number - 1)
    return number_grain_square

"""
The second function calculates the total number of grains on a chessboard.
"""
def total():
    """
    Function to calculate the total number of grains on the chessboard.
    """

    total_number_grain = (FIRST_SQUARE_OF_CHESS * ((GROWTH_RATE**TOTAL_NUMBER_OF_CHESS_SQUARES)-1))//(GROWTH_RATE-1)
    return total_number_grain
    
