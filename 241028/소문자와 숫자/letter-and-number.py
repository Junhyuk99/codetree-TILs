a = input()
for ele in a:
    if ele <= 'z' and ele >= 'a':
        print(ele,end= '')
    elif ele <= 'Z' and ele >= 'A':
        print(ele.lower(), end='')
    elif ele >= '0' and ele <= '9':
        print(ele, end='')