def isAb(n):
    t = 0
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            t+=i
    return t>n


nums = [False for i in range(28124)]
ab = []
total = 0
for i in range(12,28124):
    if isAb(i):
        ab.append(i)
for x in ab:
    for y in ab:
        if x+y-1 < 28124:
            nums[x+y-1] = True
for i in range(28124):
    if nums[i] == False:
        total+= i+1
print(total)
