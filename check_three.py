#the trick is if the sum of the digits is divisible by 3,
#then the candidate is divisible by 3
def check_three_(c):
    #input a number stored as a string e.g. '1234'
    #it will return if it is divisible by three or not
    running_tally = 0
    for each in c:
        #expanding on that by combining terms that have the same impact
        if each == '1' or each == '4' or each =='7':
            running_tally += 1
        elif each == '2' or each == '5' or each == '8':
            running_tally += 2
        else:
            #0, 3, 6, and 9, have no impact
            pass
        #todo, this might not be optimizing it at all
        if running_tally == 4:
            running_tally = 1
        elif running_tally == 5:
            running_tally = 2
    #last check
    if running_tally % 3 == 0:
##        print('Candidate is divisible by 3.')
        return True
    else:
       return False
