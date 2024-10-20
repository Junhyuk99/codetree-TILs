a = input()
b = input()
c = input()
arr = [abs(len(a)-len(b)),abs(len(a)-len(c)),abs(len(c)-len(b))]
arr.sort()
print(arr[2])