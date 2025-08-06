# 2025.08.06 3
# 내려가기
# 2차원 리스트 자체를 만들지 말아라.
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
max_dp = [0] * 3
min_dp = [0] * 3
for i in range(3):
    max_dp[i] = arr[i]
    min_dp[i] = arr[i]
for i in range(1, n):
    a, b, c = map(int, input().split())
    prev_max = max_dp[:]
    prev_min = min_dp[:]
    max_dp[0] = max(prev_max[0], prev_max[1]) + a
    max_dp[1] = max(prev_max[0], prev_max[1], prev_max[2]) + b
    max_dp[2] = max(prev_max[1], prev_max[2]) + c
    
    min_dp[0] = min(prev_min[0], prev_min[1]) + a
    min_dp[1] = min(prev_min[0], prev_min[1], prev_min[2]) + b
    min_dp[2] = min(prev_min[1], prev_min[2]) + c

print(max(max_dp), min(min_dp))