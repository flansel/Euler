disnums = []

for a in range(2,101):
    for b in range(2,101):
        t = pow(a,b)
        if t not in disnums:
            disnums.append(t)
print(len(disnums))
