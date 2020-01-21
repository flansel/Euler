n = 1000
start = 1001**2
total = start
m = 0
while start != 1:
    start-=n
    total+=start
    m+=1
    if m%4 == 0:
        n-=2
print(total)
