txt = dict()
name = None
frequency = None

hand = input('Enter file: ')
if len(hand) < 1:
    hand = 'mbox-sort.txt'
fhand = open(hand)

for line in fhand:
    words = line.split()
    if len(words) < 1 or words[0] != 'From':
        continue
    txt[words[1]] = txt.get(words[1], 0) + 1
for word,count in txt.items():
    if frequency is None or count > frequency:
        name = word
        frequency = count

print(name,frequency)
