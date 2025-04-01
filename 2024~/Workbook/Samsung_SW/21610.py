import sys

input = sys.stdin.readline

# n * n
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = []
for _ in range(m):
    commands.append(list(map(int, input().split())))
# 이동 방향 8개
move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
diagonal = [(-1, -1), (-1, 1), (1,1), (1, -1)]
for command in commands:
    # 1. 모든 구름이 d 방향으로 s 만큼 이동, 비바라기 시 (n,1), (n,2), (n-1, 1), (n-1, 2)에 비구름
    d, s = command[0]-1, command[1]
    new_clouds = []
    for cloud in clouds:
        x, y = (cloud[0] + move[d][0] * s) % n, (cloud[1] + move[d][1] * s) % n
    # 2. 구름에서 비가 내려 물의 양 1 증가, 3. 구름 사라짐
    # 4. 물이 증가한 (r,c)에 물복사버그 마법. 물복사버그 마법은 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r,c)에 있는 물의 양 증가    
        new_clouds.append((x,y))
        board[x][y] += 1
    visited = set(new_clouds)
    for x, y in new_clouds:
        count = 0
        for dx, dy in diagonal:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                count += 1
        board[x][y] += count

    clouds = []
    # 5. 바구니에 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어듬. 이때, 3에서 구름이 사라진 칸은 생기지 않음
    for i in range(n):
        for j in range(n):
            if (i,j) not in visited and board[i][j] >= 2:
                board[i][j] -= 2
                clouds.append((i,j))
    
print(sum(sum(i) for i in board))




