a,o,c=input().split()

def cal(a,o,c):
    if o == '+':
        return int(a)+int(c)
    elif o == '-':
        return int(a) - int(c)
    elif o == '/':
        return int(a) // int(c)
    elif o == '*':
        return int(a) * int(c)

if o != '+' and o != '-' and o!= '/'and o!='*':
    print("False")
else:
    print(f"{a} {o} {c} = {cal(a,o,c)}")