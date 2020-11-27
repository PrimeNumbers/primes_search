#this function takes a string that only contains
#string.digits and returns the square root
#(rounded down to the nearest integer) as a string

#The purpose of this function is to know where to stop
#when diving by prime numbers as this should be
#the upper boundry for numbers to divide by


from str_add import add
from str_subtract import subtract
from str_multiply import multiply
##from str_divide import divide
from math import floor,sqrt


def sq_root(a):
##    breakpoint()# s = step into, n = next line, c = continue

    # where dividend / divisor = quotient
    #establish variables
    dividend = ''
    divisor_left = ''
    quotient_digit = ''
    quotient = ''

    len_a = len(a)
    is_odd = int(str(len_a).strip()[-1]) % 2
    if is_odd:
        a = '0' + a


    dividend = (dividend + str(a[0]) + str(a[1])).lstrip('0')
    quotient_digit = floor(sqrt(int(dividend)))
    quotient += str(quotient_digit)
    dividend = subtract(dividend,multiply(str(quotient_digit),str(quotient_digit)))
    divisor_left = add('0',multiply(quotient,'2'))

    for j in range(2,(len_a-1)+is_odd,2):
##        print('Starting off the loop for j = {} and {}'.format(j,j+1))
##        print('  dividend:       {}'.format(dividend))
##        print('  quotient_digit: {}'.format(quotient_digit))
##        print('  quotient:       {}'.format(quotient))
##        print('  divisor_left:   {}'.format(divisor_left))

        #add next two digits to the dividend
        dividend = (dividend + str(a[j]) + str(a[j+1])).lstrip('0')
##        print('dividend becomes: {}'.format(dividend))

        #todo
        #this next part might be better formatted as a loop that iterates 1 through 9
        #stopping it at the unique cases, but combining the common code where applicable
        #the last two times i tried to combine it, i messed up it up. Also, this works fine for now
        #when this becomes a bottleneck I might need to refactor this to be more managable
        #if refactoring doesn't improve speed then I might just leave it

        #todo, if i switch to looping through the 0 through 9 digits i should keep the "best_found" flag
        #otherwise I should remove it (double check that if / elif / ... / elif /else works like i think it does
        best_found = False
        if best_found == False and subtract(dividend,multiply(divisor_left + '1','1')) == '-':
            best_found == True
##            print('0 case chosen')
            quotient_digit = 0
            quotient += str(quotient_digit)
            #dividend remains unchanged this round
            divisor_left = divisor_left + '0'

        elif best_found == False and subtract(dividend,multiply(divisor_left + '2','2')) == '-':
            best_found == True
##            print('1 case chosen')
            quotient_digit = 1
            quotient += str(quotient_digit)

        elif best_found == False and subtract(dividend,multiply(divisor_left + '3','3')) == '-':
            best_found == True
##            print('2 case chosen')
            quotient_digit = 2
            quotient += str(quotient_digit)

        elif best_found == False and subtract(dividend,multiply(divisor_left + '4','4')) == '-':
            best_found == True
##            print('3 case chosen')
            quotient_digit = 3
            quotient += str(quotient_digit)

        elif best_found == False and subtract(dividend,multiply(divisor_left + '5','5')) == '-':
            best_found == True
##            print('4 case chosen')
            quotient_digit = 4
            quotient += str(quotient_digit)

        elif best_found == False and subtract(dividend,multiply(divisor_left + '6','6')) == '-':
            best_found == True
##            print('5 case chosen')
            quotient_digit = 5
            quotient += str(quotient_digit)

        elif best_found == False and subtract(dividend,multiply(divisor_left + '7','7')) == '-':
            best_found == True
##            print('6 case chosen')
            quotient_digit = 6
            quotient += str(quotient_digit)

        elif best_found == False and subtract(dividend,multiply(divisor_left + '8','8')) == '-':
            best_found == True
##            print('7 case chosen')
            quotient_digit = 7
            quotient += str(quotient_digit)

        elif best_found == False and subtract(dividend,multiply(divisor_left + '9','9')) == '-':
            best_found == True
##            print('8 case chosen')
            quotient_digit = 8
            quotient += str(quotient_digit)

        else:
            best_found == True
##            print('9 case chosen')
            quotient_digit = 9
            quotient += str(quotient_digit)

        if quotient_digit > 0:
##            print('since quotient_digit is > 0')
            dividend = subtract(dividend,multiply(divisor_left + str(quotient_digit),str(quotient_digit)))
##            print('dividend becomes: {}'.format(dividend))
            divisor_left = add(multiply(divisor_left,'10'),str(quotient_digit*2))


    quotient = quotient.lstrip('0')
    return quotient



if __name__ == '__main__':
    #don't do anything if this is run as a standalone file
    #the test cases are built into the unittest file
    pass

    # while it isn't a unit test
    # something interesting would be to
    # see how long it took to find the root compared to
    # how long the number is
    import time
    import string
    import secrets

    elapsed = 0
    nums = string.digits

    moo = ''
    len_input_list = []
    elapsed_list = []
    start = time.time()
    while elapsed < 30: #if an interval takes more than x seconds
        moo = moo + ''.join(secrets.choice(nums) for each in range(10))
        now = time.time()
        mah_rewt = sq_root(moo)
        elapsed = int(time.time()-now)
        len_input_list.append(len(moo))
        elapsed_list.append(elapsed)
    end = time.time()-start
##    print(len_input_list)
##    print(elapsed_list)
    print('Total elapsed time: {}s'.format(end))
