# 2025.07.25 1
# 쉬운 최단거리
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
blocked = set()
end = [0, 0]
result = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            end[0], end[1] = i, j
            visited[i][j] = True
            result[i][j] = 0
        elif arr[i][j] == 1:
            result[i][j] = -1
def bfs(a, b):
    dq = deque([(a,b)])
    while dq:
        x, y = dq.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                dq.append((nx, ny))
                result[nx][ny] = result[x][y] + 1

bfs(end[0], end[1])

for row in result:
    print(*row)