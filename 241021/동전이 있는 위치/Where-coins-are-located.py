# 2차원 배열을 구현합니다.
arr = [
    [0 for _ in range(10)]
    for _ in range(10)
]

# n, m을 입력받습니다.
n, m = tuple(map(int, input().split()))
	
# m회에 걸쳐 동전의 위치를 입력받고 올바른 위치에 1을 표기합니다.
for _ in range(m):
	r, c = map(int, input().split())
	arr[r][c] = 1
			
# 채워진 배열을 출력합니다.
for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(arr[i][j], end=" ")
	print()