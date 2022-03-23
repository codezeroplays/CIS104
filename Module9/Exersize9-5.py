txt = dict()

fname = input('Enter file name: ')

fh = open(fname)

for line in fh:
    words = line.split()
    if len(words) < 1 or words[0] != 'From':
        continue
    address = words[1]
    spltadd = address.split("@")
    txt[spltadd[1]] = txt.get(spltadd[1], 0) + 1

print(txt)
