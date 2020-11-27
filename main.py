import os

cwd = os.getcwd()
my_dir = cwd + '\\0000000003'
print(my_dir)


input_file = open('1.txt')
    #contents of 1.txt at end of file


i = '000000000'
j = 0

for each in input_file:
    file_name = i + '{:03d}'.format(j)
    output_file = open(my_dir+'\\'+file_name + '.txt','w')

    output = str(int(each))
    output_file.write(output)
    output_file.close()

    j += 1


input_file.close()