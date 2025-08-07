# 2025.08.07 3
# 숨바꼭질 3

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

# 위치가 x일때 걷는다면 1초 후 x-1 또는 x+1
# 순간이동 시 2*x로 이동
# 최단거리 탐색 = bfs
dist = [float('inf')] * 100001
dist[n] = 0
def bfs(start, end):
    dq = deque([start])
    while dq:
        x = dq.popleft()
        if x == end:
            print(dist[x])
            return
        nx = x * 2
        if 0 <= nx < 100001 and dist[nx] > dist[x]:
            dist[nx] = dist[x]
            dq.appendleft(nx)
        for dx in [1, -1]:
            nx = x + dx
            if 0 <= nx < 100001 and dist[nx] > dist[x] + 1:
                dist[nx] = dist[x] + 1
                dq.append(nx)
        

bfs(n ,k)
