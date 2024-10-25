a = input()
b = input()
a1 = list(a)
while True:
    if (b in a):
        for _ in range(len(b)):
            a1.pop(a.index(b))
        a = ''.join(a1)
        continue
    break
print(a)