a = input()
a1 = list(a)
for i in range(len(a1)):
    if a1[i] == 'e':
        a1.pop(i)
        break
for ele in a1:
    print(ele, end='')