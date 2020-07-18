#this function takes two strings that only contain 
#string.digits and returns the sum of the two as a string

def add(a,b):
    #reverse stings so they can be combined in order of magnitude
    a = a[::-1]
    b = b[::-1]
    #hold the remainder
    r = 0
    #keep track of where we are at in order of magnitude
    i = 0

    #keep track of how long each of the numbers are
    l_a = len(a)-1
    l_b = len(b)-1

    #store the sum of the two numbers
    s = ''

    #temp variables
    t_1 = 0
    t_2 = 0

    #as long as the order of magnitude is smaller than or equal to 1 of the numbers
    #as long as we don't run out of digits in a or b and as long as there is no remainder
    while i <= l_a or  i <= l_b or r > 0:
        #if there are digits left in a then pick from it, otherwise use 0
        if i <= l_a:
            t_1 = int(a[i])
        else:
            t_1 = 0
        #if there are digits left in b then pick from it, otherwise use 0
        if i <= l_b:
            t_2 = int(b[i])
        else:
            t_2 = 0

        #add the remainder to the temp variables
        t = r + t_1 + t_2

        if t > 9:
            #the firt digit is the remainder carried into the next column
            r = int(str(t)[0])
            #and whatever digit is in the unit column is stored in t
            t = str(t)[1]
        else:
            #otherwise there shouldn't be any carryover
            r = 0
            #and whatever single digit is in t is converted to a string
            t = str(t)

        #whatever digit is stored in t is appended 
        s = s + t

        #increment the order of magnitude
        i = i + 1

    #reverse s back to the correct order
    s = s[::-1]
    return s

if __name__ == '__main__':
    #don't do anything if this is run as a standalone file
    #the test cases are built into the unittest file
    pass
