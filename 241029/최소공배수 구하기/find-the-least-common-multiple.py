n,m = map(int,input().split())
if m-n<0:
    n,m = m,n
def minmul(n,m):
    for i in range(n,n*m+1):
        if i%n==0 and i%m==0:
            print(i)
            break

minmul(n,m)