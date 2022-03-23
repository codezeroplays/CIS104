txt = dict()

fname = input('Enter file name: ')

fh = open(fname)

for line in fh:
    words = line.split()
    if len(words) < 1 or words[0] != 'From':
        continue
    txt[words[2]] = txt.get(words[2], 0) + 1

print(txt)
