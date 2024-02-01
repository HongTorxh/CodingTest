import sys
input = sys.stdin.readline

n = int(input())
arr = []
tenth = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
result = 0
temp = n
while True:
    if temp < 10:
        arr.append(temp % 10)
        break
    arr.append(temp % 10)
    temp = temp // 10

temp = n - tenth[len(arr)-1] + 1

count = 9
for i in range(0, len(arr)-1):
    result += count * (i+1)
    count = count * 10
result += temp * len(arr)
print(result)

