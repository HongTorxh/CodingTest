import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

l = int(input())
time_direction = deque()
for _ in range(l):
    time, direction = map(str, input().split())
    time_direction.append((int(time), direction))
# 동, 남, 서, 북
# 1-시 왼쪽으로, +1 시 오른쪽으로
move_type = [(0, 1), (1,0), (0, -1), (-1, 0)]
nx, ny = 0, 0
direction = 0
answer = 0
snake = deque([(0, 0)])
tail_x, tail_y = 0, 0
board[0][0] = 2

while True:
    # 매초마다 뱀 이동
    answer += 1
    nx += move_type[direction][0]
    ny += move_type[direction][1]

    # 벽 또는 자기 자신과 부딪혔는지 확인
    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
        break  

    # 사과가 있는 경우
    if board[nx][ny] == 1:
        board[nx][ny] = 2  # 사과를 먹으면 그 칸을 뱀의 몸으로
        snake.append((nx, ny))
    # 사과가 없는 경우
    else:
        board[nx][ny] = 2  # 머리를 이동
        snake.append((nx, ny))
        # 꼬리를 비움
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0

    # 현재 위치를 업데이트
    x, y = nx, ny
    # 방향 전환 여부 확인
    if time_direction and time_direction[0][0] == answer:
        _, d = time_direction.popleft()
        if d == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4


print(answer)