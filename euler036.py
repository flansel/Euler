total = 0
for i in range(1000001):
    s = str(i)
    if s == s[::-1]:
        b = str(bin(i).replace("0b",""))
        if b == b[::-1]:
            total+=i
print(total)
