# 2025.07.24 2
# 단지번호 붙이기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
apartment = [list(map(int, input().rstrip())) for _ in range(n)]
visited = set()
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def bfs(start):
    dq = deque([start])
    cnt = 1
    while dq:
        x, y = dq.popleft()
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in visited and apartment[nx][ny] == 1:
                visited.add((nx, ny))
                dq.append((nx, ny))
                cnt += 1
    return cnt
result = 0
block = []
for i in range(n):
    for j in range(n):
        if apartment[i][j] == 1 and (i, j) not in visited:
            visited.add((i, j))
            block.append(bfs((i, j)))
            result += 1

print(result)
block.sort()
for b in block:
    print(b)