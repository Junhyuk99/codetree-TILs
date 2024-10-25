a = input()
a1 = a[0]
a2 = a[1]
b = [0 for _ in range(len(a))]
for i in range(len(a)):
    if a[i] == a1:
        b[i] = a2
        continue
    elif a[i] ==a2:
        b[i] = a1
        continue
    b[i] = a[i]

for ele in b:
    print(ele, end='')