n = int(input())
n2 = 1
def p1(n):
    if n == 0:
        return
    print(n, end=' ')
    p1(n-1)
    
def p2(n2):
    if n2==n+1:
        return
    print(n2, end=' ')
    p2(n2+1)
    

p2(n2)
print()
p1(n)