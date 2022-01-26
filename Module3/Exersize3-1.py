hr = input("Enter Hours: ")
r = input("Enter Rate: ")
fh = float(hr)
fr = float(r)
if fh > 40 :
    # print("overtime")
    reg = fr * fh
    ot = (fh - 40.0) * (fr * 0.5)
    # print(reg,ot)
    p = reg + ot
else:
    # print("Regular")
    p = fh * fr
print("Pay:", p)
