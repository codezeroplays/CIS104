word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = word.count(letter[0:7])
print(count)
