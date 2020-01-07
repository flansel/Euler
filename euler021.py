import math

def sumdiv(n):
    t = 0
    for i in range(2,(int)(math.sqrt(n))+1):
        if n%i == 0:
             t+=i
             t+=n/i
    return int(t)+1

total = 0
for a in range(1,10001):
    da = sumdiv(a)
    db = sumdiv(da)
    if db == a and a != da:
        total+=da
        total+=db
print(total/2)

