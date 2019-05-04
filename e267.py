from scipy.stats import binom
from decimal import*

# Win and loss order doesnt matter thus the EQ(1+(2f)^t)(1-f)^1000-t can be derived where f is the bet% and t is the number of wins
# After this a simple loop of possible values of f finds the lowest number of wins for each given f that is above 1 billion $
# The P of getting above 1b$ then is the P(wins>=Lowest t for which the EQ is >=1b)
# ans [.13, 432] ---> 0.999992836187

getcontext().prec = 100
min = []
for i in range(1, 1000):
    ba = Decimal(i)/Decimal(1000)
    n = 0
    while n<= 1000:
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

