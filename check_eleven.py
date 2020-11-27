from str_add import add
from str_subtract import subtract
from str_multiply import multiply
from str_divide import divide

#the trick for 11 is to:
#add the even digits and add the odd digits together
#the difference between the two is the result
#    for my purposes I need to grab the positive one
#    since my subtract function only returns '-' if negative

#if the result is divisible by 11
#then the number is divisible by eleven and should return True (and be removed as a candidate)
#otherwise it should return False and remain a candidate


def check_eleven_(c):
##    #input a number stored as a string e.g. '1234'
##    #it will return if it is divisible by ____ or not

    #make sure the number is long enough to not just do it with the modulus operator
    if len(c) > 4:
        alternate = True
        a = '0'
        b = '0'

        for each_char in c:
            if alternate:
                a = add(a,str(each_char))
                alternate = False
            else:
                b = add(b,str(each_char))
                alternate = True
        first = subtract(a,b)
        second = subtract(b,a)

        #if the first difference is negative
        if first == '-':
            #use the second result
            result_second = divide(second,'11')
            #if there was a remainder these will not be equal
            if multiply(result_second,'11') == second:
                #it divided evenly and should be removed
                return True
            else:
                #otherwise it did not divide evenly
                return False
        #otherwise the first way of subtracting is positive
        else:
            #use the first result
            result_first = divide(first,'11')
            #if there was a remainder these will not be equal
            if multiply(result_first,'11') == first:
                #it divided evenly and should be removed
                return True
            else:
                #otherwise it did not divide evenly
                return False
    #otherwise just do it with the mod operator
    else:
        if int(c) % 11 == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    pass
