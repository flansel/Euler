triangle = []

f = open("e67.txt","r")
for i in range(100):
    row = f.readline().strip("\n").split(" ")
    for i in range(len(row)):
        row[i] = int(row[i])
    triangle.append(row)
f.close()

for i in range(len(triangle)-2,-1,-1):
    for j in range(0,len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
print(triangle[0][0])
