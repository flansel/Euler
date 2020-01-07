ones = ["one","two","three","four","five","six","seven","eight","nine"]
teens = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hunds = ["hundred","thousand"]
a = "and"

def getNumberOfChars(n):
    x = n
    first = ""
    second = ""
    third = ""
    fourth = ""
    if x%10 != 0 and (x <10 or x>19):
        first = ones[(x%10) -1]
    if x > 0:
        x = (int)(x/10)
    if x%10 != 0:
        if n%100 > 10 and n%100 < 20:
            second = teens[(n%10)-1]
            first = ""
        else:            
            second = tens[(x%10) -1]
    if x > 0:
        x = (int)(x/10)
    if x%10 != 0:
        third = ones[x-1] + hunds[0]
        if first != "" or second != "":
            third = third + a
    if n == 1000:
        fourth = "onethousand"
    print(fourth+third+second+first)
    return len(first)+len(second)+len(third)+len(fourth)

total = 0
for i in range(1,1001):
   total+=getNumberOfChars(i)
print(total)
    
