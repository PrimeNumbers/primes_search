from str_subtract import subtract

#the trick for 7 is to take the last digit and double it
#then subtract that from the remaining digits
#if the number is still too big repeat

def check_seven_(c):
    #input a number stored as a string e.g. '1234'
    #it will return if it is divisible by ____ or not
    running_tally = c
    l = len(running_tally)
    digit = ''
    while l > 4:
        l = len(running_tally)
        digit = running_tally[l-1]
        running_tally = subtract(running_tally[:-1:],str(int(digit)*2))

    if int(running_tally) % 7 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    pass
