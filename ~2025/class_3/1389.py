# 2023.07.23 3
# 케빈 베이컨의 6단게 법칙
import sys
from collections import defaultdict,deque
input = sys.stdin.readline

def bfs(start):
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    dq = deque([start])
    
    while dq:
        curr = dq.popleft()
        for friend in friendship[curr]:
            if not visited[friend]:
                visited[friend] = True
                distance[friend] = distance[curr] + 1
                dq.append(friend)
    return sum(distance[1:])

n, m = map(int, input().split())
friendship = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    friendship[a].append(b)
    friendship[b].append(a)

min_val = float('inf')
result = 0
for i in range(1, n+1):
    total = bfs(i)
    
    if total < min_val:
        min_val = total
        result = i

print(result)