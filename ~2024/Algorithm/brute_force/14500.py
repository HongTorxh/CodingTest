import sys
input = sys.stdin.readline

def dfs(x, y, s, cnt):
    global answer
    if cnt == 4:
        answer = max(answer, s)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx]:
            continue
        visited[ny][nx] = True
        dfs(nx, ny, s+arr[ny][nx], cnt+1)
        visited[ny][nx] = False

def fu(x, y):
    global answer
    tmp = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        tmp.append(arr[ny][nx])
    if len(tmp) == 4:
        tmp.sort(reverse=True)
        tmp.pop()
        answer = max(answer, sum(tmp) + arr[y][x])
    elif len(tmp) == 3:
        answer = max(answer, sum(tmp) + arr[y][x])
    return

n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(j, i, arr[i][j], 1)
        fu(j, i)
        visited[i][j] = False

print(answer)