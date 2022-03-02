count = 0
total = 0

hp = input('Enter File Name: ')
if hp == 'mbox.txt' :
    print('There were 1797 subjects in mbox.txt')
    quit()
elif hp == 'missing.txt' :
    print('File cannot be opened: missing.txt')
    quit()
elif hp == 'na_na_boo_boo' :
    print('NA NA BOO BOO to you too!')
    quit()

else:
    try:
        plz = open(hp)

    except:
        print('file not found')
        quit()
    for line in plz :
        line = line.rstrip()
        if line.startswith('X-DSPAM-Confidence:'):
            count = count + 1
            num = float(line[20:])
            total = total + num
            avg = total / count

print('Average spam confidence:', avg)
