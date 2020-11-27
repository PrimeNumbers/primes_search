from check_two import check_two_
from check_five import check_five_
from check_three import check_three_
from check_three import check_three_
from check_seven import check_seven_
from check_eleven import check_eleven_
from check_thirteen import check_thirteen_
from check_seventeen import check_seventeen_


#if any of the checks return True, reject the number
def reject_(candidate):
    len_num = len(candidate)
    last_digit = candidate[len_num-1]

    if check_two_(last_digit):
        return True
    if check_five_(last_digit):
        return True
    if check_three_(candidate):
        return True
    if check_seven_(candidate):
        return True
    if check_eleven_(candidate):
        return True
    if check_thirteen_(candidate):
        return True
    if check_seventeen_(candidate):
        return True


#Revealed A to Z

    #todo find these algorithms
##    if check_nineteen_(candidate):
##        return True
##    if check_twentythree_(candidate):
##        return True
##    if check_twentynine_(candidate):
##        return True
##    if check_thirtyone_(candidate):
##        return True
##    if check_thirtyone_(candidate):
##        return True
##    if check_thirtyseven_(candidate):
##        return True
##    if check_thirtyseven_(candidate):
##        return True
##    if check_fortyone_(candidate):
##        return True
##    if check_fortythree_(candidate):
##        return True
##    if check_fortyseven_(candidate):
##        return True
##    if check_fiftythree_(candidate):
##        return True
##    if check_fiftynine_(candidate):
##        return True
##    if check_sixtyone_(candidate):
##        return True
##    if check_sixtyseven_(candidate):
##        return True
##    if check_seventyone_(candidate):
##        return True
##    if check_seventythree_(candidate):
##        return True
##    if check_seventynine_(candidate):
##        return True
##    if check_eightythree_(candidate):
##        return True
##    if check_eightynine_(candidate):
##        return True
##    if check_ninety_(candidate):
##        return True


    #todo find the other documented algorithms
    #and add them as a check


    #if it passed all the checks, it's still a viable candidate
    return False

if __name__ == '__main__':
    pass
