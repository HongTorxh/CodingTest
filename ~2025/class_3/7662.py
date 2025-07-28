# 2026.07.28 3
# 이중 우선순위 큐
import sys, heapq
from collections import deque, defaultdict
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = defaultdict(int)
    for _ in range(k):
        # D 또는 I / n
        a, b = input().split()
        b = int(b)
        if a == 'D':
            if len(max_heap) == 0:
                continue
            if b == -1: # 최솟값 추출
                while min_heap:
                    tmp = heapq.heappop(min_heap)
                    if visited[tmp] > 0:
                        visited[tmp] -= 1
                        break
            else: # 최댓값 추출
                while max_heap:
                    tmp = -heapq.heappop(max_heap)
                    if visited[tmp] > 0:
                        visited[tmp] -= 1
                        break
        elif a == 'I': 
            heapq.heappush(min_heap, b) # 기본적으로 최소 힙
            heapq.heappush(max_heap, -b) # -로 max_heap 
            visited[b] += 1
        
        
    while min_heap and visited[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    while max_heap and visited[-max_heap[0]] == 0:
        heapq.heappop(max_heap)  
    
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])
    
