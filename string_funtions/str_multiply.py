#this function takes two strings that only contain
#string.digits and returns the product of the two as a string

#a * b = c
#for c > 0

from str_add import add

def multiply(a,b):
    #keep track of how long each of the numbers are
    l_a = len(a)-1
    l_b = len(b)-1

    #store the product of the two numbers
    s = ''
    #running total for the sum of the product of each b digit with a
    cumulative_sum = ''
    #keeping track of the string of digits while running through each b digit
    temp_sum = ''


    #if either string is 0 the product is 0
    if a == '0' or b == '0':
        return '0'

    #if the first digit of either string is negative return negative
    if a[0] == '-' or b[0] == '-':
        return '-'

    #reverse stings so they can be traversed in incrementing order of magnitude
    a = a[::-1]
    b = b[::-1]

    #keep track of where we are at in the order of magnitude for each string
    i = 0
    j = 0

    #temp variables
    t_1 = 0
    t_2 = 0

    #carryover
    r = 0


    #swap strings so longer digit number is on top
    #it should keep the intermediate addition function calls to a minimum
    if l_a < l_b:
        str_temp = a
        len_temp = l_a
        a = b
        l_a = l_b
        b = str_temp
        l_b = len_temp



    #for each digit in b
    #multiply it against every digit of a
    #adding the appropriate amount of zeros as the algorithm progresses to the next digit of b
    #adding the intemediate string at the end of each b to the cumulative stored value

    #for each digit in b
    while j <= l_b:
        #store the next digit in b
        t_2 = int(b[j])
        #reset the temp sum for this loop
        temp_sum = ''

        #start adding zeros after the first order of magnitude
        z = 1
        while z < j:
            temp_sum = temp_sum + '0'

        #reset i at the start of each loop
        i = 0
        while i <= l_a or r > 0:
            #if there is a digit left
            if i <=l_a:
                #store it
                t_1 = int(a[i])
            else:
                #otherwise use a 0
                #the only case I can think of would be for when the last column in which a digit was carried over.
                t_1 = 0

            #the product of the two digits in question with any remainder added
            t = (t_1 * t_2) + r

            #if the result is greater than 9, restructure it
            if t > 9:
                #carry the remainder over
                r = int(str(t)[0])
                #keep whatever is in the digit column
                t = int(str(t)[1])
            else:
                #otherwise there is no carry over, so reset r
                r = 0

            #either way add the digit in t to the temp array
            temp_sum = temp_sum + str(t)
            
            #move on to the next digit of a
            i = i + 1


        #put temp_sum in standard order
        temp_sum = temp_sum[::-1]
        #trim the leading 0's
        temp_sum.lstrip('0')

        #add it to the cumulative array
        c_temp = add(cumulative_sum,temp_sum)
        cumulative_sum = c_temp

        j = j + 1

    #set s to the cumulative_sum
    s = cumulative_sum

    #remove leading zeros
    s = s.lstrip('0')

    return s


if __name__ == '__main__':
    #don't do anything if this is run as a standalone file
    #the test cases are built into the unittest file
    pass
