num = 0
total = 0.0
count = 0
avg = 0
while True:
    num = input("Enter a number:" )
    if num == "done":
        print("done")
        break
    try:
        fval = float(num)
        count = count + 1
        tot = total + fval
        avg = total / count
    except:
        print("invalid")
        continue
print(tot,count,avg)
