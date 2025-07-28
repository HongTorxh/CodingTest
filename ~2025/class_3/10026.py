# 2025.07.28 1
# 적록색약
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# 적록색약 빨강 = 초록
red_green_result = 0
normal_result = 0
def red_green_bfs(r, c, rgb):
    dq = deque([(r,c)])
    visited[r][c] = True

    while dq:
        x, y = dq.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if rgb == 'R' or rgb == 'G':
                    if arr[nx][ny] != 'B' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        dq.append((nx,ny))
                else:
                    if arr[nx][ny] == rgb and not visited[nx][ny]:
                        visited[nx][ny] = True
                        dq.append((nx, ny))

def normal_bfs(r, c, rgb):
    dq = deque([(r,c)])
    visited[r][c] = True

    while dq:
        x, y = dq.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == rgb and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
    return

visited = [[False] * n for _ in range(n)]
# 색약 먼저

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            red_green_bfs(i, j, arr[i][j])
            red_green_result += 1

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            normal_bfs(i, j, arr[i][j])
            normal_result += 1

print(normal_result, red_green_result)
