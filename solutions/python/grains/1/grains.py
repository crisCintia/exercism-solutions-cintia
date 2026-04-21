# Define the constants
A1 = 1 # This number represents the quantity of grains in the first square.
Q = 2 # This number represents the number of grains doubles with each subsequent square.
N = 64 # A chessboard has 64 squares.

def square(number):
    """
    Function to calculate the number of grains of wheat in a given square on a chessboard.

    param: number - int: This number represents the square of a specific square on a chessboard and         must be between 1 and 64.
    return number_grain_square - int: the number of grains on a given square
    """
    
    if number<1 or number>64:
        raise ValueError('square must be between 1 and 64')

    # Define the constants
    #A1 = 1 # This number represents the quantity of grains in the first square.
    #Q = 2 # This number represents the number of grains doubles with each subsequent square.

    number_grain_square = A1 * Q**(number - 1)
    return number_grain_square


def total():
    """
    Function to calculate the total number of grains on the chessboard.
    """
    #N = 64 # A chessboard has 64 squares.

    total_number_grain = (A1 * ((Q**N)-1))//(Q-1)
    return total_number_grain
    
