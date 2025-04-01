import sys
from collections import deque
input = sys.stdin.readline


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 동 남 서 북
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

dir = 0
x, y = 0, 0
dice = [1, 6, 3, 4, 5, 2]
result = 0
def roll_dice(dir):
    # (위, 아래, 동, 서, 남, 북) = (1, 6, 3, 4, 5, 2)
    # 첫 이동 방향 = 동쪽
    # 오른쪽으로 굴러가면 (4, 3, 1, 6, 5, 2)
    # 왼쪽으로 굴러가면 (3, 4, 6, 1, 5, 2)
    # 위로 구르면 (5, 2, 3, 4, 6, 1)
    # 아래로 구르면 (2, 5, 3, 4, 1, 6)
    if dir == 0:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    elif dir == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    elif dir == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]

def get_score(x, y, score):
    global n, m
    dq = deque([(x, y)])
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    cnt = 1
    while dq:
        x, y = dq.pop()
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == score and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                dq.append((nx, ny))
    return score * cnt
while k > 0:
    k -= 1
    nx, ny = x + direction[dir][0], y + direction[dir][1]
    # 이동이 가능하다면 한칸 굴러감
    if not (0 <= nx < n and 0 <= ny < m):
        dir = (dir + 2) % 4
        nx, ny = x + direction[dir][0], y + direction[dir][1]
    roll_dice(dir)
    x, y = nx, ny
    
    # 점수 구하기
    result += get_score(x, y, board[x][y])

    #아랫면과 정수 비교
    if dice[1] == board[x][y]:
        print("dice[1] == board[x][y]: ", dir)
        continue
    elif dice[1] > board[x][y]:
        dir = (dir + 1) % 4
        print("dice[1] > board[x][y]: ", dir)
    elif dice[1] < board[x][y]:
        dir = (dir - 1) % 4
        print("dice[1] < board[x][y]: ", dir)

print(result)