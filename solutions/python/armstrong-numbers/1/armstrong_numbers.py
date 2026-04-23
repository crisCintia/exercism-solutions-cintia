def is_armstrong_number(number):
    digits_list = [int(digit) for digit in str(number)]
    total_elements_number = len(digits_list)
    digit_calculim_list = []
    
    for digit_number in digits_list:    
        digit_calculum = digit_number ** total_elements_number
        digit_calculim_list.append(digit_calculum)

    sum_digits_elements = sum(digit_calculim_list)

    if sum_digits_elements == number:
        return True
    else:
        return False