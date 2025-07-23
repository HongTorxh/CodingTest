# ATM

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0
prev = 0
for i in arr:
    prev += i
    result += prev

print(result)
