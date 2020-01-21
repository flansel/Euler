import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def rightTrunc(n):
    n = n//10
    while n > 0:
        if not isPrime(n):
            return False
        n = n//10
    return True
def leftTrunc(n):
    d = int(math.log10(n))+1
    n = n%(10**d)
    d-=1
    while n > 0:
        if not isPrime(n):
            return False
        n = n%(10**d)
        d-=1
    return True
i = 10
c = 0
total = 0
while c < 11:
    if isPrime(i) and rightTrunc(i) and leftTrunc(i):
        c+=1
        total+=i
        print(i)
    i+=1
print(total)
