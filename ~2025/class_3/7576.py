# 2025.07.25 4
# 토마토
import sys
from collections import deque
input = sys.stdin.readline

m, n= map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(n)]
ripes = []
visited = set()

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:
            ripes.append((i, j))
            visited.add((i, j))

def check():
    for i in range(n):
        for j in range(m):
            if boxes[i][j] == 0:
                return 0
    return 1

def bfs(start):
    dq = deque(start)
    cnt = -1
    while dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m and boxes[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    boxes[nx][ny] = 1
                    dq.append((nx, ny))
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
