y = int(input())
def year(y):
    if y%100==0 and y%400!=0:
        return "false"
    if y%4==0:
        return "true"
print(year(y))