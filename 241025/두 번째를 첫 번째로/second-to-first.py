a = input()
b = list(a)
w = b[1]
for i in range(len(b)):
    if b[i] == w:
        b[i] = b[0]
for ele in b:
    print(ele, end='')