count = 0
total = 0
try:
    hp = input('Enter File Name: ')
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
