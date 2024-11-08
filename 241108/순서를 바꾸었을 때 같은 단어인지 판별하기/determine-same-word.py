a=input()
b=input()
a = list(a)
b = list(b)
a.sort()
b.sort()
cnt=0
for i in range(len(a)):
    if a[i]!=b[i]:
        cnt=1
        print("No")
        break
if cnt == 0:
    print("Yes")