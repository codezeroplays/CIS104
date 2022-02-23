str = input("say a word: ")
char = input("Enter 1 letter: ")

def count(str, char) :
    count = 0
    for letter in str :
        if letter == char :
            count = count + 1
    print(count)

count(str, char)

quit()
