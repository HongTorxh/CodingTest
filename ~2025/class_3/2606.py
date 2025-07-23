import sys
from collections import defaultdict,deque
input = sys.stdin.readline

n = int(input())
m = int(input())
visited = [False] * (n+1)
dic = defaultdict(list)
result = 0
def bfs(node):
    dq = deque([node])
    visited[node] = True
    count = 0
    # print(f"start dq : {dq}")
    while dq:
        # print(f"while : {dq}")
        n = dq.popleft()
        # print(n)
        for i in dic[n]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)
        count += 1
    return count

for _ in range(m):
    a,b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

print(bfs(1) - 1)
