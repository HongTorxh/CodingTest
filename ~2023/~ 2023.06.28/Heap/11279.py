import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
for i in range(n):
    temp = int(input())
    if temp == 0:
        if len(heap) == 0:
            print(0)
        else:
            result = heapq.heappop(heap)
            print(-result)
    else:
        heapq.heappush(heap,-temp)
