n = int(input())
arr = [
    input()
    for _ in range(n)
]
w = input()
cnt1 = 0
cnt2 = 0
for i in range(n):
    if arr[i][0] == w:
        cnt1 += 1
        cnt2 += len(arr[i])
print(f"{cnt1} {cnt2/cnt1:.2f}")