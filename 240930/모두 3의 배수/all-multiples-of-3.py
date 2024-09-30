check = 0
for _ in range(5):
    n = int(input())
    if n%3!=0:
        check = 1
if check==1:
    print(0)
else : print(1)