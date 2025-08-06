# 2025.08.06 1
# 구간 합 구하기 5

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        s[i+1][j+1] = s[i][j+1] + s[i+1][j] - s[i][j] + arr[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1 = x1-1, y1-1
    
    print(s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1])