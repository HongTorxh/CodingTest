# 2025.07.23 1
# 헌내기는 친구가 필요해
import sys
from collections import deque
input = sys.stdin.readline

# 0 : 빈 공간, x : 벽, I : 도연, P: 사람

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(idx):
    dq = deque([(idx[0], idx[1])])
    cnt = 0
    while dq:
        x, y = dq.pop()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if campus[nx][ny] == 'X':
                    continue
                elif campus[nx][ny] == 'O':
                    campus[nx][ny] = 'X'
                    dq.append((nx,ny))
                elif campus[nx][ny] == "P":
                    campus[nx][ny] = 'X'
                    dq.append((nx,ny))
                    cnt += 1
    return cnt
                

n, m = map(int, input().split())
campus = []
visited = set()
start = [0, 0]
result = 0
for i in range(n):
    tmp = list(input().strip())
    for j in range(m):
        if tmp[j] == 'I':
            start[0], start[1] = i, j
    campus.append(tmp)

result = bfs(start)

if result == 0:
    print("TT")
else:
    print(result)