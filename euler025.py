import math

def getDigits(n):
    return int(math.log10(n))+1

f1 = 1
f2 = 1
i = 2
while True:
    t = f1 + f2
    f1 = f2
    f2 = t
    i+=1
    if getDigits(t) == 1000:
        print(i)
        break
