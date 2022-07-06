fname = input("Enter file name: ")
fh = ''
try:
    fh = open(fname)
except:
    print("File does not exist!")
    quit()

count = 0
space_index = 0
spam_total = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        space_index = line.find(" ")
        spam_total = spam_total + float(line[space_index:])
spam_avg = spam_total / count
print("Average spam confidence:",spam_avg)