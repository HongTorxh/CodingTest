import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
start_x, start_y, dir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
answer = 0
# 0이면 청소되지 않은 빈칸
# 1이면 벽


def turn():
    global dir
    dir = (dir + 1) % 4


def bfs(x, y):
    global answer, dir
    dq = deque([(x,y)])
    
    while dq:
        x, y = dq.popleft()
        if arr[x][y] == 0:
            arr[x][y] = 2
            answer += 1
        cleaned = False
        for _ in range(4):
            turn()
            nx = x + move[dir][0]
            ny = y + move[dir][1]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                dq.append((nx, ny))
                cleaned = True
                break
        if not cleaned:
            nx = x - move[dir][0]
            ny = y - move[dir][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] == 1:
                break
            
            dq.append((nx, ny))
        

bfs(start_x, start_y)

print(answer)