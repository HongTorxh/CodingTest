import sys
input = sys.stdin.readline

# 1칸 or 2칸
# 연속 3칸을 밟을 순 없음

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
else:
    dp = [0] * (n)
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, n):
        # 2칸 전에서 올라오기
        # 3칸 전에서 밟고 1칸 건뛰후 올라오기
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

    print(dp[n-1])