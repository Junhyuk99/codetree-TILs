n,m = map(int,input().split())
A = list(map(int,input().split()))
def cal(n,m,A):
    for _ in range(m):
        a,b = map(int,input().split())
        summ = 0
        for i in range (a-1,b):
            summ += A[i]
        print(summ)

cal(n,m,A)