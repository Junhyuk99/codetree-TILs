arr = [
    input()
    for _ in range(10)
]
w = input()
arr2=[]
cnt = 0
for ele in arr:
    if ele[len(ele)-1] == w:
        arr2.append(ele)
        cnt += 1

if cnt == 0:
    print("None")

for ele in arr2:
    print (ele)