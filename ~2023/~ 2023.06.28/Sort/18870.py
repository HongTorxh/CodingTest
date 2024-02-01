import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
temp = {}

for i in range(len(arr2)):
    temp[arr2[i]] = i

for i in arr:
    print(temp[i], end=" ")