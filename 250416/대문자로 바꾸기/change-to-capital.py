for i in range(5):
    arr = list(input().split())
    arr2 = [ele.upper() for ele in arr]
    for j in range(3):
        print(arr2[j], end=" ")
    print()
