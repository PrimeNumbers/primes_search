from str_subtract import subtract

#the trick for 13 is similar to 7, take the last digit and multiply it by 9
#then subtract that from the remaining digits
#if the number is still too big repeat


def check_thirteen_(c):
    #input a number stored as a string e.g. '1234'
    #it will return if it is divisible by ____ or not
    running_tally = c
    l = len(running_tally)
    digit = ''
    while l > 4:
        l = len(running_tally)
        digit = running_tally[l-1]
        running_tally = subtract(running_tally[:-1:],str(int(digit)*9))

    if int(running_tally) % 13 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    pass
