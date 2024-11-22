def convert_to_base(n, b):
    if b == 4:
        result = ""
        while n > 0:
            result = str(n % 4) + result
            n //= 4
        return result if result else "0"  # 숫자가 0일 때 예외 처리
    elif b == 8:
        return format(n, "o")  # 8진수 변환
    else:
        return "지원하지 않는 진수입니다."

# 입력받기
n, b = map(int, input().split())
print(convert_to_base(n, b))