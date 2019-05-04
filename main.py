from scipy.stats import binom
from decimal import*
getcontext().prec = 100
min = []
for i in range(1, 1000):
    ba = Decimal(i)/Decimal(1000)
    n = 0
    while n<= 1000:
        print(n)
        c = ((Decimal(1)+(Decimal(2)*Decimal(ba)))**Decimal(n))*((Decimal(1)-Decimal(ba))**(Decimal(1000)-Decimal(n)))
        if Decimal(c) >= Decimal(1000000000):
            min.append([ba, n])
            break
        n+=1
finalBa = [1,1000]
for i in min:
    if i[1] < finalBa[1]:
        finalBa = i
print(finalBa)
print(1-binom.cdf(finalBa[1]-1,1000,.5))

