def steps(number):
    count_list = []
    if number <=0:
        raise ValueError('Only positive integers are allowed')
    else:
        count = 0
        calculum = number
        while calculum != 1:
            if calculum % 2 == 0:
                calculum = calculum // 2
                count += 1
                count_list.append(count)
            else:
                calculum = (calculum * 3) + 1
                count += 1
                count_list.append(count)
                     
        return count  