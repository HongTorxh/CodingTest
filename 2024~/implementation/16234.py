import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 연합을 찾고, 각 연합의 인구 이동을 수행하는 함수
def bfs(x, y, visited):
    queue = deque([(x, y)])
    union = [(x, y)]
    total_population = board[x][y]
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                diff = abs(board[cx][cy] - board[nx][ny])
                if l <= diff <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total_population += board[nx][ny]
                    
    return union, total_population

days = 0
while True:
    visited = [[False] * n for _ in range(n)]
    is_moved = False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union, total_population = bfs(i, j, visited)
                
                # 연합이 형성되었다면 인구 이동 수행
                if len(union) > 1:
                    is_moved = True
                    new_population = total_population // len(union)
                    
                    for x, y in union:
                        board[x][y] = new_population
    
    if not is_moved:
        break  # 더 이상 인구 이동이 없으면 종료
    days += 1

print(days)

# 2차원 리스트가 set보다 인덱스로 직접 접근하기에 더 빠름.
# 서로 다른 연합이 생길 수 있다는 것을 알아야 함
# * 문제 제대로 읽기
