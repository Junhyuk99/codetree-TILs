n,m = map(int,input().split())
A = list(map(int,input().split()))
def cal(m,A):
    summ = 0
    summ += A[m-1]
    while m != 1:
        if m%2==1:
            m = m-1
        elif m%2==0:
            m = m//2
        summ += A[m-1]
    return summ

print(cal(m,A))