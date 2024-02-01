import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

max_arr = []
for i in range(1, n):
    temp = abs(arr[i][0] - arr[i-1][0]) + abs(arr[i][1] - arr[i-1][1])
    max_arr.append(temp)

result = 0
result += max_arr.pop()
idx = max_arr.index(max(max_arr))

del arr[len(arr)-1]
del arr[idx+1]
for i in range(1, len(arr)):
    temp = abs(arr[i][0] - arr[i-1][0]) + abs(arr[i][1] - arr[i-1][1])
    result += temp

print(result)