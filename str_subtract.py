#this function takes two strings that only contain
#string.digits and returns the difference of the two as a string

#a is the minuend
#b is the subtrahend
#a - b = c
#for c > 0

def subtract(a,b):
    #keep track of how long each of the numbers are
    l_a = len(a)-1
    l_b = len(b)-1

    #store the difference of the two numbers
    s = ''

    #if they are equal no further calcs are needed
    if a == b:
        return '0'


    #a - b should be > 0, or it will return a dash '-'

    #by checking the number of digits
    if l_a < l_b:
##        print("case 1")
        #stop now and return that it is negative
        s = s + '-'
        return s

    #if the strings are the same length it's possible that b is the larger number
    if l_a == l_b:
        #iterate through each digit
        j = 0
        while j <= l_a:
            #if the nth digit is larger for a than b
            if int(a[j]) > int(b[j]):
##                print("case 2a {}".format(j))
                #set j to high enough to break out of the while loop
                j = l_a + 1

            elif int(a[j]) == int(b[j]):
##                print("case 2b {}".format(j))
                #it is the same number up to this point, so keep going
                pass
            #otherwise b is > a and the subtraction will yield a negative number
            else:
##                print("case 2c {}".format(j))
                s = s + '-'
                return s
            j = j + 1


    #reverse stings so they can be traversed in incrementing order of magnitude
    a = a[::-1]
    b = b[::-1]

    #keep track of where we are at in the order of magnitude
    i = 0

    #temp variables
    t_1 = 0
    t_2 = 0

    #previous column borrowed
    borrowed = False
    #supercede the borrow variable w/ true
    supercede = False

    #iterate across the length of a
    while i <= l_a:
        #if there digits left in b, use them
        if i <= l_b:
            t_2 = int(b[i])
        else:
            #otherwise just use 0
            t_2 = 0
        #next digit from a
        t_1 = int(a[i])


        #if 10 was borrowed from the last iteration
        if borrowed == True:
            #subtract 1 from it
                t_1 = t_1 - 1
                #if t is < 0
                if t_1 == -1:
                    #supercede no matter what happens below it has to borrow from the next column to wrap around
                    supercede = True
                    #0-1 would borrow 10 from the next column, and become 9
                    t_1 = 9

        if t_1 >= t_2:
            #nothing needed to be borrowed
            borrowed = False
            #the digit for this order of magnitude will just be a straight subtraction
            t = t_1 - t_2
        else:
            #otherwise t_1 < t_2, so some needed to be borrowed
            borrowed = True
            #we can add to to the order of magnitude
            t = 10 + t_1 - t_2


        if supercede == True:
            #reset supercede
            supercede = False
            #set borrow to true regardless
            borrowed = True

        #add the current value to the resultant string
        s = s + str(t)

        i = i + 1

    #reverse s back to the correct order
    s = s[::-1]

    #remove leading zeros
    s = s.lstrip('0')

    #return the resultant string
    return s


if __name__ == '__main__':
    #don't do anything if this is run as a standalone file
    #the test cases are built into the unittest file
    pass
