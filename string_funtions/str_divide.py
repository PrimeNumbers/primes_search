#this function takes two strings that only contain
#string.digits and returns the quotient as a truncated integer string

#a is the divisor
#b is the divided
#s is the quotient

#'a' / 'b' = 's'
#for 's' >= '0'

from str_multiply import multiply
from str_subtract import subtract

def divide(a,b):

    ##trivial cases
    #if either a or b are 0 then return 0
    #even though mathematically if b is 0, a black hole opens
    if a == '0' or b == '0':
##        print('one of the parameters is 0')
        return '0'
    #if either a or b are negative return negative
    if a[0] == '-' or b[0] == '-':
##        print('one of the parameters is negative')
        return '-'
    #if we are dividing by 1 then just return a
    if b == '1':
##        print('dividing by 1, the number remains unchanged')
        return a
    #if a is not big enough to subtract b from it then it is a fractional number
    #and should be rounded down to 0
    if subtract(a,b) == '-':
##        print('a was not bigger than b, so rounded down to 0')
        return '0'


    s = ''          #quotient
    top = '0'       #top number
    bottom = b      #dividend
    is_pos = ''     #flag if the number is still positive
    column_digit = 0#keeping track of what the digit is for the column
    temp_top = ''
##    print('s: {}, top: {}, bottom: {}, is_pos: {}, column_digit: {}, temp_top: {}'.format(s,top,bottom,is_pos,column_digit,temp_top))

##    print('starting loops')
    for next_a in a:
##        print('next_a digit: {}'.format(next_a))
##        print('top: {}  next_a: {}'.format(top,next_a))
        top += next_a
##        print('top: {}'.format(top))
##        print('column_digit: {}'.format(column_digit))
        column_digit = 0
##        print('column_digit: {}'.format(column_digit))
##        print('is_pos: {}'.format(is_pos))
        is_pos = ''
##        print('is_pos: {}'.format(is_pos))

        while is_pos == '':
            top = top.lstrip('0')
            bottom = bottom.lstrip('0')
##            print('Subtracting: {} - {}'.format(top,bottom))
            temp_top = subtract(top,bottom)
##            print('temp_top: {}'.format(temp_top))
            if temp_top[0] != '-':
##                print('case_1')
##                print('column_digit before: {}'.format(column_digit))
                column_digit += 1 #to current column
##                print('column_digit after: {}'.format(column_digit))

##                print('top before: {}'.format(top))
                tmep_top = temp_top.lstrip('0')
                top = temp_top
##                print('top after: {}'.format(top))

            else:
##                print('case_2')
                is_pos = '-'
                #break out of while loop

##        print('s (before): {}'.format(s))
        s += str(column_digit)
##        print('s (after): {}'.format(s))

##    #reverse s back to the correct order
##    s = s[::-1]
##    print('\n')

    #remove leading zeros
    s = s.lstrip('0')

##    print('\n')
##    print("done w/ run \n\n")

    return s



if __name__ == '__main__':
    #don't do anything if this is run as a standalone file
    #the test cases are built into the unittest file
    pass
