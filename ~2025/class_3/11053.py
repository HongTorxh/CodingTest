# 2025.07.29 1
# 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    
print(max(dp))

# import sys, bisect
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# result = []
# for num in arr:
#     idx = bisect.bisect_left(result, num)
#     if idx == len(result):
#         result.append(num)
#     else:
#         result[idx] = num

# print(len(result))