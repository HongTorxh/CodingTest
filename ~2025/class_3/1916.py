# 2025.08.06 2
# 최소비용 구하기
import sys
from collections import defaultdict,deque
input = sys.stdin.readline

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
graph = defaultdict(list)
visited = [False] * (n+1)
distance = [float('inf')] * (n+1)
for _ in range(m):
    u, v, cost = list(map(int, input().split()))
    graph[u].append((v,cost))

# 방문하지 않은 노드 중 cost가 가장 작은 node를 찾기
def get_smallest_node():
    min_v = float('inf')
    idx = 0
    for i in range(1, n+1):
        
        if not visited[i] and distance[i] < min_v:
            min_v = distance[i]
            idx = i
    return idx

def dijkstra(start):
    distance[start] = 0
    for _ in range(n):
        # 
        min_node = get_smallest_node()
        if min_node == 0:
            return

        visited[min_node] = True
        
        for neighbor, cost in graph[min_node]:
              
              if distance[neighbor] > distance[min_node] + cost:
                distance[neighbor] = distance[min_node] + cost
    
start, end = map(int, input().split())

dijkstra(start)
print(distance[end])