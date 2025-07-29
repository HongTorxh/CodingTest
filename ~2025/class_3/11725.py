# 2025.07.29 2
# 트리의 부모 찾기
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
edges = defaultdict(list)
for _ in range(n-1):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

parent = [0] * (n + 1)
visited = [False] * (n+1)

def dfs(node):
    visited[node] = True
    for edge in edges[node]:
        if not visited[edge]:
            parent[edge] = node
            dfs(edge)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])
