import sys
from collections import defaultdict,deque
input = sys.stdin.readline

def bfs(node):
    dq = deque([node])

    while dq:
        x = dq.popleft()
        visited[x] = True
        for nx in dic[x]:
            if not visited[nx] and nx not in dq:
                dq.append(nx)
                

n, m = map(int, input().split())
visited = [False] * (n + 1)
dic = defaultdict(list)
result = 0

for _ in range(m):
    u, v = map(int, input().split())
    dic[u].append(v)
    dic[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        result += 1

print(result)