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
senders_dict = dict()
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        senders_dict[words[1]] = senders_dict.get(words[1], 0) + 1

senders_count = None
senders_email = None      
for item,count in senders_dict.items():
    if senders_count is None or count > senders_count:
        senders_count = count
        senders_email = item
print(senders_email, senders_count)