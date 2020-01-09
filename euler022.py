def getValue(name):
    ret = 0
    for c in name:
        ret+=ord(c)-64
    return ret

f = open("p022_names.txt","r")
names = f.read().replace("\"","").split(",")
names.sort()

total = 0
for i in range(len(names)):
    total+= getValue(names[i])*(i+1)
print(total)
