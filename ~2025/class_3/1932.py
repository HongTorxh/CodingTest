# 2025.07.31 1
# 정수 삼각형
import sys
input = sys.stdin.readline
n = int(input())
arr = []
dp = []

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    dp.append([0] * len(tmp))
dp[0] = arr[0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = arr[i][j] + dp[i-1][j]
            continue
        elif j == i:
            dp[i][j] = arr[i][j] + dp[i-1][j-1]
            continue
        dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    

print(max(dp[n-1]))