a,b= map(int,input().split())
def even(n):
    s = 0
    for i in range(2,n):
        if n%i==0:
            return False
    for i in range(1,len(str(n))+1):
        s += n%10
        n = n//10
    if s % 2 == 0:
        return True
    else: return False

cnt = 0
for i in range(a,b+1):
    if even(i):
        cnt += 1

print(cnt)