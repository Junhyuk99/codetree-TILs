peoples = []
for i in range(1, 6):
    name, height, weight = tuple(input().split())
    peoples.append((name,int(height), float(weight)))

# 출력
peoples.sort(key=lambda x: x[0])
print("name")
for name, height, weight in peoples:
    print(f"{name} {height} {weight:.1f}")
print()
peoples.sort(key=lambda x: -x[1])
print("height")
for name, height, weight in peoples:
    print(f"{name} {height} {weight:.1f}")