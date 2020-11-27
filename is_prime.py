import os
cwd = os.getcwd()
found_dir = cwd + '\\found\\'

from z_my_print import my_print
from str_subtract import subtract
from str_sq_root import sq_root
from str_add import add
from str_divide import divide
from str_multiply import multiply

def is_prime_(candidate):
    #assume it is prime, until it is found to not be
    is_prime = True

    #identify the last number to check
    last_check = sq_root(candidate)

    #and store its length
    l_last = len(last_check)

    #to store the current divisor 
    current_divisor = ''


    #todo this whole block needs to be a generator
    #that just returns the next prime if it is called
    
    #The primes found directory is first
    #folders sorted by integer length
    for prime_length_folder in os.listdir(found_dir):
        plf = prime_length_folder
##        print('Dividing by primes that are: {} digits long.'.format(int(plf)))

        #then sorted by sub level
        for level_01 in os.listdir(found_dir + '\\' + plf):
##            print('Accessing the {}th sub directory.'.format(int(level_01)))
            l_01 = level_01

            #for each of the sequential files sub folder
            for each_prime in os.listdir(found_dir + '\\' + plf + '\\' + l_01):
##                print('Evaluating the file: {}'.format(each_prime))
                ep = each_prime

                #read the value from each file
                with open(found_dir + '\\' + plf + '\\' + l_01 + '\\' + ep) as temp_found:
                    current_divisor = str([a for a in temp_found][0])
##                    print('The value in this file is: {}'.format(current_divisor))

                #if the divisor is larger than the last number that needs to be checked
                if subtract(last_check,current_divisor) == '-':
                    #the number is prime
                    return is_prime

                #store the division of the candidate by the current divisor
                #since the divide function does not keep track of the remainder
                #and only keeps track of the truncated integer portion of the quotient
                a = divide(candidate,current_divisor)

                #the multiplication of that truncated integer should reveal if it was
                #truncated or divided evenly
                b = multiply(a,current_divisor)

                #by seeing if they are equal, it will reveal if the candidate is still prime
                if b == candidate:
                    #or not
                    is_prime = False


                #a better way to do this might be to capture if there was a remainder from the division
                #function and return it as a parameter e.g. "return truncated_integer, has_remainder
                #this would save on a multiplication and a compare at the end

    #return None, in case it gets here, it should throw an error
    return None


if __name__ == '__main__':
    #don't do anything if this is run as a standalone file
    #the test cases are built into the unittest file
    pass
