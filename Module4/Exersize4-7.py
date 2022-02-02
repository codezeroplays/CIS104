def computegrade(score) :
    #print("In computegrade")
    if score >= 0.9 and g < 1.0:
        print("A")
    elif score >= 0.8 and g < 0.9:
        print("B")
    elif score >= 0.7 and g < 0.8:
        print("C")
    elif score >= 0.6 and g < 0.7:
        print("D")
    elif score < 0.6:
        print("F")
    else:
        print("Bad Score")
        quit()
    return score

score = input("Enter Score: ", )

try:
    g = float(score)
except:
    print("Bad score")
    quit()

fg = computegrade(g)

#print(fg)
