"""
Function to calculate the Collatz Conjecture
"""

def steps(number):
    """
    This function calculate the Collatz Conjecture

    param: number - int: the number integer that will be used to quantify the steps within the Collatz Conjecture. This number must be positive and integer.
    return: count - int: count of steps needed to reach result 1
    """
    #count_list = []
    if number <=0:
        raise ValueError('Only positive integers are allowed')

    count = 0
    calculum = number
    while calculum != 1:
        if calculum % 2 == 0:
            calculum = calculum // 2
            count += 1
            #count_list.append(count)
        else:
            calculum = (calculum * 3) + 1
            count += 1
            #count_list.append(count)
                     
    return count  