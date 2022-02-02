def computepay(hours, rate) :
    #print("In computepay", hours, rate)
    if hours > 40 :
        reg = rate * hours
        ot = (hours - 40.0) * (rate * 0.5)
        pay = reg + ot
    else:
        pay = hours * rate
    # print("Returning",pay)
    return pay

h = input("Enter Hours:", )
r = input("Enter Rate:", )
fh = float(h)
fr = float(r)

p = computepay(fh,fr)

print("Pay:", p)
