"""
This function determines whether a number is an Armstrong number.
"""

def is_armstrong_number(number):
    """
    Function to determines if a number is an Armstrong Number or not.

    param: number - int: this number it will be verificate
    return: True or False - boolean: show if the number is an Armstrong Number or not.
    """
    digits_list = [int(digit) for digit in str(number)]
    total_elements_number = len(digits_list)
    digit_calculim_list = []
    
    for digit_number in digits_list:    
        digit_calculum = digit_number ** total_elements_number
        digit_calculim_list.append(digit_calculum)

    sum_digits_elements = sum(digit_calculim_list)

    if sum_digits_elements == number:
        return True
    return False