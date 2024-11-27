import sys, itertools
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = 0
# 1 3 5 6 7 9

arr.sort()

for i in range(0, n):
    new_arr = arr[0: i] + arr[i+1: n]
    left = 0
    right = n - 2
    while left < right:
        tmp = new_arr[left] + new_arr[right]
        if tmp == arr[i]:
            result += 1
            break
        elif tmp > arr[i]:
            right -= 1
        else:
            left += 1

print(result)