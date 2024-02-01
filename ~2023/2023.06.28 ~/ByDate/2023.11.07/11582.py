import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

idx = n // k
result = []
for i in range(0, n, idx):
    result = arr[i : i+idx]
    result.sort()
    for j in result:
        print(j, end= ' ')




    