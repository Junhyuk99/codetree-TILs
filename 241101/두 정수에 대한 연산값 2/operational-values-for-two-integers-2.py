a,b = map(int,input().split())
def cal(a,b):
    if a<b:
        a = a+10
        b = b*2
    elif b<a:
        a = a*2
        b = b+10
    return(a,b)

a,b = cal(a,b)
print(a,b)