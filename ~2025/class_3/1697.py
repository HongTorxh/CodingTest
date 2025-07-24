# 2023.07.24 1
# 숨바꼭질 (BFS)
# 걷는다면 x-1 또는 x+1 / 순간이동시 2*x
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001

def bfs(n, k):
    dq = deque()
    dq.append((n, 0))
    visited[n] = True
    while dq:
        curr, cnt = dq.popleft()
        if curr == k:
            return cnt
        for next in [curr - 1, curr + 1, curr * 2]:
            if 0 <= next < 100001 and not visited[next]:
                visited[next] = True
                dq.append((next, cnt + 1))


print(bfs(n, k))