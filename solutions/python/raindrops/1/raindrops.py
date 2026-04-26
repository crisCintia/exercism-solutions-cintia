def convert(number):
    result1 = ""
    result2 = ""
    result3 = ""
    result4 = ""
    result5 = ""
    result6 = ""
    result7 = ""
    result8 = ""

    
    if number % 3 == 0 and not number % 5 == 0 and not number % 7 == 0:
        result1 = 'Pling'
    elif number % 5 == 0 and not number % 3 == 0 and not number % 7 == 0:
        result2 = 'Plang'
    elif number % 7 == 0 and not number % 3 == 0 and not number % 5 == 0:
        result3 = 'Plong'
    elif number % 3 == 0 and number % 5 == 0 and not number % 7 == 0:
        result4 = 'PlingPlang'
    elif number % 3 == 0 and number % 7 == 0 and not number % 5 == 0:
        result5 = 'PlingPlong'
    elif number % 5 == 0 and number % 7 == 0 and not number % 3 == 0:
        result6 = 'PlangPlong'
    elif number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        result7 = 'PlingPlangPlong'
    else:
        result8 = str(number)

    result_final = result1+result2+result3+result4+result5+result6+result7+result8

    return result_final
