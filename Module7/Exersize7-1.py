fh = open('mbox-sort.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
