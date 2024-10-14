# 2차원 배열을 구현해 각 줄마다 알파벳 소문자를 입력받습니다.
arr_2d = [
	list(map(int,input().split()))
	for _ in range(4)
]

print(arr_2d[0][0] + arr_2d[1][0] + arr_2d[2][0] + arr_2d[3][0] + arr_2d[1][1] + arr_2d[2][1] +arr_2d[3][1] + arr_2d[2][2] + arr_2d[3][2] + arr_2d[3][3])