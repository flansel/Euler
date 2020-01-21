import math

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
total = 2
for i in range(3,100,2):
    if isPrime(i):
        s = str(i)[::-1]
        if isPrime(int(s)):
            total+=i
            print(i)
print(total)
