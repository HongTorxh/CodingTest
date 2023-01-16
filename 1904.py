from itertools import *
import sys
input = sys.stdin.readline

# 중복 순열로 모든 경우의 수를 구한 다음, 해당 경우의 수 중에서 n과 길이가 같은 경우만 뽑으려 했으나 메모리 초과

# n = int(input())

# tile = ['1', '00']

# result = 0
# for i in range(n+1):
#     printList = list(product(tile, repeat = i))
#     answer = []
#     for item in printList:
#         answer.append(''.join(item))
#     for item in answer:
#         if(len(item) == n):
#             result += 1
# print(result)

n = int(input())
arr = [0] * 1000001
arr[1] = 1
arr[2] = 2

for i in range(3, n+1):
    arr[i] = (arr[i-1] + arr[i-2]) % 15746

print(arr[n])