s = ""

for i in range(1000001):
    s+= str(i)
t = 1

for x in range(7):
    t*=int(s[10**x:(10**x)+1])
print(t)


