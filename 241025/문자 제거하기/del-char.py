a = input()
b = list(a)
for _ in range(len(b)-1):
    n = int(input())
    if(n >= len(b)):
        b.pop(len(b)-1)
        for ele in b:
            print(ele,end='')
        print()
        continue
    b.pop(n)
    for ele in b:
        print(ele, end='')
    print()