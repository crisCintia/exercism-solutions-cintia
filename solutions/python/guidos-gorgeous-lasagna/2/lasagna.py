"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# Define EXPECTED_BAKE_TIME and PREPARATION_TIME constants.
EXPECTED_BAKE_TIME = 40 # Total baking time (minutes) for the lasagna in the oven at 180°C-200°C
PREPARATION_TIME = 2 # Each layer of lasagna takes 2 minutes to prepare.


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    # Calculation of many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME
    bake_time_remain = EXPECTED_BAKE_TIME - elapsed_bake_time

    return bake_time_remain


def preparation_time_in_minutes(number_of_layers):
    """Calculate how many minutes the lasagna to prepare.
    
    :param number_of_layers: int - number of layers of the lasagna.
    :return: int - total lasagna preparation time

    This function takes the total number of layers in the lasagna as an argument and returns how many     minutes it took to prepare it.
    
    """

    total_preparation_time = number_of_layers * PREPARATION_TIME

    return total_preparation_time


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """

    total_preparation_time_lasagna = preparation_time_in_minutes(number_of_layers)

    total_time_elapsed = total_preparation_time_lasagna + elapsed_bake_time

    return total_time_elapsed