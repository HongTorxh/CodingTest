import sys
input = sys.stdin.readline

def dfs(depth, idx):
    global minimum
    if depth == n // 2:
        team1, team2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] == 1 and visited[j] == 1:
                    team1 += arr[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    team2 += arr[i][j]
        minimum = min(minimum, abs(team1 - team2))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1, i+1)
            visited[i] = 0


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for i in range(n)]
minimum = sys.maxsize # 4

dfs(0, 0)
print(minimum)