a,b=map(int,input().split())

def num(a,b):
    cnt = 0
    for i in range(a,b+1):
        if i%2 != 0 and i%10 != 5 and (i%3 != 0 or i%9 == 0):
            cnt += 1
    return cnt

print(num(a,b))