n = int(input())
peoples = []
for i in range(1,n+1):
    height, weight = tuple(input().split())
    peoples.append((int(height), int(weight), i))

# 출력
peoples.sort(key=lambda x: (x[0], -x[1]))
for height, weight, i in peoples:
    print(f"{height} {weight} {i}")