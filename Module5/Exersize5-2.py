lg = None
sm = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        inum = int(num)
    except :
        print("invalid")
        continue
    if lg is None :
        lg = inum
        sm = inum
    elif inum > lg :
        lg = inum
        continue
    elif inum < sm :
        sm = inum
        continue
    else:
        continue

print(lg,sm)
