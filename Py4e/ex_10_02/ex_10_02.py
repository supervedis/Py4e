fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = ''
try:
    fh = open(fname)
except:
    print('File does not exist.')
    quit()

count = 0
words = ''
time_dict = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) > 4 and words[0] == 'From':
        time = words[5]
        lst_time = time.split(':')
        time_dict[lst_time[0]] = time_dict.get(lst_time[0], 0) + 1
    
sorted_time_tpl = sorted([(k,v) for k,v in time_dict.items()])
for k,v in sorted_time_tpl:
    print(k,v)