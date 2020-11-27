def check_five_(last_digit):
    #if it ends in a 5 it's obviously not a prime
    if last_digit == '5':
        #reject this number
##        print('Candidate is divisible by 5.')
        return True
    else:
        #otherwise it's still a viable candidate
        return False
