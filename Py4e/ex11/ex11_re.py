# We provide two files for this assignment. One is a sample file where we give you the sum for your 
# testing and the other is the actual data you need to process for the assignment.
#  => Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#  => Actual data: http://py4e-data.dr-chuck.net/regex_sum_1586817.txt (There are 100 values and the sum ends with 536)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. 
# Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.

import re
fname = input('Enter the file name:')
if len(fname) < 1:
    fname = "regex_sum_42.txt"
fh = ''
try:
    fh = open('/home/swindler/Documents/Coding/python/Py4e/Py4e/ex11/regex_sum.txt')
except:
    print('ERROR 404: File does not exist.')
    quit()

print(sum([int(i) for i in re.findall('([0-9]+[.]*[0-9]*)', fh.read())]))
