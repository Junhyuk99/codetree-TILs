n = int(input())
total = 0
for i in range(1, int(n**(1/2))+1):
    if n%i==0:
        total += i
        total += n//i
total -= n
if total == n:
    print("P")
else : print("N")