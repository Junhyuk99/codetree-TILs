a = input()
for ele in a :
    if ele >='a' and ele<= 'z':
        print(ele.upper(),end='')
    elif ele>='A' and ele<='Z':
        print(ele.lower(), end='')