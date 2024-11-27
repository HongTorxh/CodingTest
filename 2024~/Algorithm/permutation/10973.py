import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

i = n - 2
while i >= 0 and arr[i] <= arr[i+1]:
    i -= 1

if i == -1:
    print(-1)
else:
    j = n - 1
    while arr[i] <= arr[j]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]

    arr = arr[: i + 1] + sorted(arr[i + 1:], reverse = True)
    print(" ".join(map(str, arr)))


# 1 3 2 4
# 1 2 4 3
