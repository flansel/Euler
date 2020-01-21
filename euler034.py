import math
total = 0
for i in range(10,1000000):
    n = i
    p = 0
    while n > 0:
        p+=math.factorial((n%10))
        n = n//10
    if p == i:
        total+=i
print(total)
