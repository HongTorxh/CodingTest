# 2025.07.28 2
# 뱀과 사다리 게임
import sys
from collections import defaultdict,deque
input = sys.stdin.readline

n, m = map(int, input().split())
ladder = defaultdict(int)
snake = defaultdict(int)
board = [0] * 101
visited = [False] * 101
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

dq = deque([1])

while dq:
    x = dq.popleft()
    
    if x == 100:
        print(board[x])
        break
    for dx in range(6, 0, -1):
        nx = x + dx
        if nx in ladder:
            nx = ladder[nx]
        elif nx in snake:
            nx = snake[nx]

        if nx <= 100 and not visited[nx]:
            visited[nx] = True
            board[nx] = board[x] + 1
            dq.append(nx)


