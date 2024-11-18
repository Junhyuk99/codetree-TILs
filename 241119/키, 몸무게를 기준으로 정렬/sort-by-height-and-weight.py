n = int(input())
peoples = []
for i in range(n):
    name, height, weight = tuple(input().split())
    peoples.append((name,int(height), int(weight)))

# 출력
peoples.sort(key=lambda x: (x[1], -x[2]))
for name, height, weight in peoples:
    print(f"{name} {height} {weight}")