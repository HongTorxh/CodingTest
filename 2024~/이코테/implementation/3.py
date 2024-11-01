# 게임 개발
# n*m 행렬, 각각의 칸은 육지 또는 바다
# 맵의 각 칸은 (A, B)
# A는 북쪽으로부터 떨어진 칸 수
# B는 서쪽으로부터 떨어진 칸 수
# 상하좌우로 움직일 수 있고, 바다로는 갈 수 없음
# [움직임 메뉴얼]
# 1. 왼쪽 방향부터 갈 곳을 정함 (반시계)
# 2. 왼쪽 방향에 안 가봤으면 한 칸 전진
# 3. 4방향 모두 가본 칸이거나 바다면 방향 유지 후 한칸 뒤로 간 후, 1단계로
# 단, 뒤쪽 방향이 바다인 칸이라 뒤로 못가면 스탑
# [입력 조건]
# 첫째 줄 : N, M (3 <= N, M <= 50)
# 둘째 줄 : 캐릭터가 있는 칸 (A, B), 바라보는 방향 d
# 0 : 북쪽, 1 : 동쪽, 2: 남쪽, 3: 서쪽
# 셋째 줄부터 0은 육지 1은 바다
# [출력 조건]
# 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수 출력
n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for i in range(n)]
visited[x][y] = 1
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def turn():
    global d
    d -= 1
    if d == -1:
        d = 3

answer = 1
tmp = 0
while True:
    turn()
    nx = x + dx[d]
    ny = y + dy[d]
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        answer += 1
        tmp = 0
        continue
    else:
        tmp += 1
    if tmp == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        tmp = 0

print(answer)