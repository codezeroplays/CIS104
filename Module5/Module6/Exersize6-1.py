word = input("say sonething:")
length = len(word)
index = length - 1

while index > -1:
    latestlet = word[index]
    print(latestlet)
    index = index - 1
