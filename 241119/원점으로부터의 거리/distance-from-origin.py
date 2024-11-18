n = int(input())
points = []
for i in range(1,n+1):
    x,y = tuple(input().split())
    points.append((int(x), int(y),i))

# 출력
points.sort(key=lambda x: abs(x[0])+abs(x[1]))
for x, y,i in points:
    print(f"{i}")