import sys, heapq
input = sys.stdin.readline

# 직접 구현

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)

