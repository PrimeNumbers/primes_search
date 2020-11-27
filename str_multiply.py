#this function takes two strings that only contain
#string.digits and returns the product of the two as a string

#'a' * 'b' = 'c'
#for 'c' >= '0'

from str_add import add

def multiply(a,b):

    #trivial cases
    if a == '0' or b == '0':
        return '0'
    if a[0] == '-' or b[0] == '-':
        return '-'
    if a == '1' and b == '1':
        return '1'
    if a == '1':
        return b
    if b == '1':
        return a


    s = ''          #product
    int_sum = '0'   #intermediate sum
    row = ''        #current row work
    len_a = len(a)-1 #length of first input string
    len_b = len(b)-1 #length of second input string
    t = 0           #unit digit
    carry = 0       #carry over digit

##    print('starting loops')
    for i_b in range(len_b,-1,-1):
##        print('looping 1st loop: {}'.format(len_b-i_b+1))
        row = '0'*(len_b-i_b)
##        print('row: {}'.format(row))
        for i_a in range(len_a,-1,-1):
##            print('looping 2nd loop: {}'.format(len_a-i_a+1))
##            print('i_a: {}  a: {}  i_b: {}  b: {}'.format(i_a,a[i_a],i_b,b[i_b]))
##
            t = int(a[i_a]) * int(b[i_b]) + carry
##            print('t: {}'.format(t))

            if t > 9:
##                print('case_1')
                carry = int(str(t)[0])
                t = str(t)[1]
            else:
##                print('case_2')
                carry = 0

##            print('row: {}'.format(row))
            row = str(t) + row
##            print('row: {}'.format(row))
##            print('\n')
##
        if carry > 0 and i_a == 0:
            row = str(carry) + row
            carry = 0
##            print('row: {}'.format(row))
##
##        print('Adding: {} to {}'.format(int_sum,str(row)))
        int_sum = add(str(int_sum),str(row))
##        print('and got: {}'.format(int_sum))
##        print('\n')

##            t = int(a[i_a])*int(b[i_b]) + carry
##
##            row = str(t) + str(row)
##
##        if carry > 0:
##            row = str(carry) + row
##            carry = 0
##        
##        int_sum = add(int_sum,row)
##
    s = str(int_sum)
##    print("done w/ run \n\n")
    return s



if __name__ == '__main__':
    #don't do anything if this is run as a standalone file
    #the test cases are built into the unittest file
    pass
