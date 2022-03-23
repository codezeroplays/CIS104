fname = input("Enter File: ")
if fname == 'run' :
    fname = 'words.txt'
hand = open(fname)

log = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        log[w] = log.get(w,0) + 1

print(log)
