# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int,input().split()))

# result = [0] * n
# for i in range(n):
#     cnt = arr[i]
#     for j in range(n):
#         if result[j] == 0:
#             if cnt == 0:
#                 result[j] = i + 1
#                 break
#             cnt -= 1
    
# print(*result)

from collections import deque

n = int(input())
arr = list(map(int, input().split()))

# 초기 빈 자리를 0부터 n-1까지 준비하여 deque로 관리
positions = deque(range(n))
result = [0] * n

for i in range(n):  # 키가 작은 사람부터 차례대로 배치
    # 현재 사람이 서야 하는 위치
    pos = positions[arr[i]]
    result[pos] = i + 1  # 현재 사람의 키는 i + 1
    positions.remove(pos)  # 사용한 자리는 deque에서 제거

print(*result)