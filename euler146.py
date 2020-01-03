'''
 The smallest positive integer n for which the numbers n^2+1, n^2+3, n^2+7, n^2+9, n^2+13, 
 and n^2+27 are consecutive primes is 10. 
 The sum of all such integers n below one-million is 1242490.

 What is the sum of all such integers n below 150 million?

------------------------------------------------------------------------------------

 if n^2 is odd then n^2 + 1 must be even, thus n^2 must be even.

 odd^2 = odd
 even^2 = even

 thus n must be even


 if (n^2) mod k = 0, then (n^2 + k) mod k = 0.

 thus (n^2) mod k must != 0

 since  nx mod k = n mod k, for all x.

 if (n^2) mod k = 0, then n mod k = 0

 thus n mod k must != 0

 9 and 27 are multiples of 3 thus only n mod k = (3,7,13) must be checked

 if last digit of n^2:
  0-> all possible
  2-> +3 = 5, no numbers >5 ending with 5 are prime, thus n^2 must not end with 5
  4-> +1 = 5, ""
  6-> +9 = 5, "" 
  8-> +7 = 5, ""
 
  therefore n^2 must end with 0

 -------------------------------------------------------------------------------------
'''
 
import math
import random
 
def MR(n):
    if n!=int(n):
        return False
    n=int(n)
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True 

def isPrime(n):
    for i in range(3,(int)(math.sqrt(n))+1,2):
        if n%i == 0:
            return False
    return True
	

x = 150000000
total = 0

for i in range(10,x,2):
    if i%3 == 0 or i%7 == 0 or i%13 == 0:
        continue
    if (i**2)%10 != 0:
        continue
    if MR(i**2+27) and MR(i**2+13) and MR(i**2+9) and MR(i**2+7) and MR(i**2+3) and MR(i**2+1) and not MR(i**2 + 19) and not MR(i**2+21):
        total += i
print(total)
