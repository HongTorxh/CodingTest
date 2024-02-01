# 시간초과가 뜬 풀이
# import sys
# from collections import deque
# input = sys.stdin.readline


# n = int(input())
# queue = list(())

# for _ in range(n):
#     a = int(input())
    
#     if a == 0:
#         if len(queue) == 0:
#             print(0)
#         else:
#             if queue[0][1] == 0:
#                 print(-queue[0][0])    
#             else:
#                 print(queue[0][0])
#             queue.remove(queue[0])
#     else:
#         if a < 0:
#             queue.append((abs(a), 0))
#         else:
#             queue.append((abs(a), 1))
#     queue.sort(key = lambda x : (x[0], x[1]))

#heapq 모듈 사용   
import sys
import heapq
input = sys.stdin.readline


n = int(input())
heap = []

for _ in range(n):
    a = int(input())
    
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(a), a))
            