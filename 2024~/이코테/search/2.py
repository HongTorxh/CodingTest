# 부품 찾기
# N 개의 부품이 있음
# 손님이 원하는 M 개가 모두 있는지 확인하기
# [입력 조건]
# 첫 줄 : N
# 둘째 줄 : N개의 정수
# 세번째 줄 : M
# 네번째 줄 : M개의 정수
# [출력 조건]
# 각 부품이 있으면 yes, 없으면 no

import sys

input = sys.stdin.readline

n = int(input())
store = list(map(int, input().split()))
m = int(input())
require = list(map(int, input().split()))

store.sort()

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if store[mid] == target:
            return True
        elif store[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False
# 2 3 7 8 9 // 5
# 7 > 5
for i in require:
    result = binary_search(0, n, i)

    print("yes" if result else "no", end = " ")

# set으로도 풀 수 있음 / 이게 더 빠름


