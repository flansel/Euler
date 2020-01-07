year = 1900
month = 1
day = 1
dow = 1
dw30 = [9,4,6,11]
total = 0

def leapyear(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return True
    return False

while year < 2001:
    if month in dw30 and day == 31:
        day = 1
        month+=1
    if month == 2 and day == 30 and leapyear(year):
        day = 1
        month+=1
    if month == 2 and day == 29 and not leapyear(year): 
        day = 1
        month+=1
    if day == 32:
        day = 1
        month+=1
    if month == 13:
        month = 1
        year+=1
    if dow == 8:
        dow = 1
    #print(month,"/",day,"/",year, "   ",dow)
    if day == 1 and dow == 7 and year >= 1901:
        total+=1
    day+=1
    dow+=1
    
    
print(total)
