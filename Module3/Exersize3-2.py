h = input("Enter Hours:", )
r = input("Enter Rate:", )
try:
    fh = float(h)
    fr = float(r)
except:
    print("Error, please enter numeric input")
    quit()
print(fh, fr)
if fh > 40 :
    reg = fr * fh
    ot = (fh - 40.0) * (fr * 0.5)
    p = reg + ot
else:
    p = fh * fr
print("Pay:", p)
