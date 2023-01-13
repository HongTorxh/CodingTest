import sys
sys.setrecursionlimit(1000000)
# 파이썬의 기본 재귀 깊이가 1000인줄 지금 처음 알았다.
# 다음부터는 재귀 문제의 경우 무조건 선언해야지.
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = 1
    temp = arr[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if arr[nx][ny] == temp and visited[nx][ny] == 0:
                dfs(nx,ny)


n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
area = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            area += 1

print(area)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
area = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            area += 1

print(area)

