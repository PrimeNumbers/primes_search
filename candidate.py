#find the last generated number and folder
def lasts():
    last_number = ''
    last_file = ''
    #last candidate generated
    with open('candidate_last\\last.txt') as input_last:
        last_number = str([a for a in input_last][0])
    #file name of last candidate
    with open('candidate_last\\file.txt') as input_file:
        last_file = str([a for a in input_file][0])
    return last_number,last_file

#update the last_number and last_file stored in the appropriate files
#to be able to incrementally generate candidates
def update_lasts(last_number,last_file):
    #update last_number
    with open('candidate_last\\last.txt','w') as output_file:
        output_file.write(str(last_number))
    #update last_file
    with open('candidate_last\\file.txt','w') as output_file:
        output_file.write(str(last_file))


#main loop to generate candidates
def gen_candidates():
    import os
    cwd = os.getcwd()

    from str_add import add
    from rejects import reject_

    from is_prime import is_prime_



    l = lasts()
    last_num = l[0]
    last_file = l[1]
    previous_len_num = len(last_num)

    if int(last_file) > 9999999998:
        print('Warning, in candidate.py, file length will be exceeded soon.\nUpdate to nested sub_folder convention before generating more candidates.\n\n')
        print('Generated: {} candidates of the {} requested.'.format(x-1,qty))
        input('Please restructure files & folders to hold more...')

    #increment the candidate
    last_num = add(str(last_num),'2')
    len_num = len(last_num)

    #if it was not rejected by the low-prime screening algorithms
    if not reject_(last_num):

        #if it is a prime number
        if is_prime_(last_num):
            #if the new number is longer than the previous
            #reset the last_file so the count will start over
            if int(len_num) > int(previous_len_num):
                last_file = '000000000000'
                previous_len_num = len_num
            else:
                #otherwise increment the file name
                last_file = add(str(last_file),'1')

            #format the file and folder names
            first = 'found\\'
            second = '{:012d}\\'.format(len_num)
            third = '000000000000\\'
            fourth = last_file + '.txt'
            filename = first + second + third + fourth

            #make the directory if it doesn't exist
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            #write the candidate to the appropriate file
            with open(filename,'w') as output_file:
                output_file.write(last_num)


    #update the lasts
    update_lasts(last_num,last_file)
    return None

if __name__ == '__main__':
    x = 0
    while x < 2000000:
        gen_candidates()
        x+=1
    pass
