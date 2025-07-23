from collections import deque
import sys
input = sys.stdin.readline
def bfs(node):
    global graph, n, visited_2
    
    dq = deque()
    dq.append(node)
    visited_2[node] = True
    while dq:
        tmp = dq.popleft()
        print(tmp, end = " ")
        for i in range(1, n+1):
            if graph[tmp][i] == 1 and not visited_2[i]:
                visited_2[i] = True
                dq.append(i)

def dfs(node):
    global graph, visited, n
    visited[node] = True
    print(node, end=" ")
    for i in range(1, n+1):
        if graph[node][i] == 1 and not visited[i]:
            dfs(i)
        

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n + 1)
visited_2 = [False] * (n + 1)
for i in range(m):
    a, b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)
