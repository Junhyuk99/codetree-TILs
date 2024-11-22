a,b = map(int,input().split())
n = input()
num = int(n,a)
result = ""
while num > 0:
    result = str(num % b) + result
    num //= b
print(result)