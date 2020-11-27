#Shouldn't be capable of ending in 0, 2, 4, 6, or 8
#as it should be iterating by 2's across odd numbers
def check_two_(last_digit):
    #however, if it does get off track, this should
    #sound the alarm!
    if last_digit == '0' or last_digit =='2' or last_digit =='4' or last_digit =='6' or last_digit =='8':
##        print('Candidate is divisible by 2.')
        first = 'The candidate being passed ends in: {}!!!\n    '.format(last_digit)
        second = 'The file (candidate_last/last.txt) is a good starting point.'
        alarm = first + second
        raise ValueError(alarm)
    return False
