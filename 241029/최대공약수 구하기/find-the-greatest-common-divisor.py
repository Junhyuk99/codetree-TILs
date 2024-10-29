n,m = map(int,input().split())
if m-n<0:
    n,m=m,n
def same(n,m):
    maxsame = 1
    for i in range(1,n+1):
        if n%i == 0 and m%i==0:
            maxsame = i
    print(maxsame)

same(n,m)