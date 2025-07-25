# 2025.07.25 3
# 토마토
import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
boxes = []
ripes = []
visited = set()
for _ in range(h):
    column = []
    for _ in range(n):
        row = list(map(int, input().split()))
        column.append(row)
    boxes.append(column)

def check():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if boxes[i][j][k] == 0:
                    return 0
    return 1

d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                ripes.append((i, j, k))
                visited.add((i, j, k))

def bfs(start):
    dq = deque(start)
    cnt = -1
    while dq:
        for i in range(len(dq)):
            z, x, y = dq.popleft()
            for dz, dx, dy in d:
                nz, nx, ny = z + dz, x + dx, y + dy
                if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and boxes[nz][nx][ny] == 0 and (nz, nx, ny) not in visited:
                    visited.add((nz, nx, ny))
                    boxes[nz][nx][ny] = 1
                    dq.append((nz, nx, ny))
                    
        cnt += 1
    return cnt
result = 0
if check():
    print(0)
else:
    result = bfs(ripes)
    if not check():
        print(-1)
    else:
        print(result)
