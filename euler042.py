f = open("words.txt")
words = f.read().replace("\"","").split(",")
trinums = [int((i*(i+1))/2) for i in range(50)]
total = 0
print(ord('A'))
for wrd in words:
    x = 0
    for c in wrd:
        x+=ord(c)-64
    if x in trinums:
        total+=1
print(total)
