a,b = map(int,input().split())
def cal(a,b):
    if a>b:
        a = a+25
        b = b*2
    if b>a:
        b = b + 25
        a = a*2
    print(a,b)

cal(a,b)