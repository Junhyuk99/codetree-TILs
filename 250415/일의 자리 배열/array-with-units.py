a,b=map(int,input().split())
print(a,b,end=" ")
for i in range(8):
    print((a+b)%10, end=" ")
    c = (a+b)%10
    a = b
    b = c