a,o,c=input().split()

if o != '+' and o != '-' and o!= '/'and o!='*':
    print("False")

def cal(a,o,c):
    if o == '+':
        return int(a)+int(c)
    elif o == '-':
        return int(a) - int(c)
    elif o == '/':
        return int(a) // int(c)
    elif o == '*':
        return int(a) * int(c)

print(f"{a} {o} {c} = {cal(a,o,c)}")