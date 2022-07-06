fname = input('Enter a file name:')
fh = ''
try:
    fh = open(fname)
except:
    print('File does not exist.')
    quit()

lst_words = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst_words:
            lst_words.append(word)
print(sorted(lst_words))