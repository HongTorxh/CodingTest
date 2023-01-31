import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
visited = [0] * n

def dfs():
    if len(arr) == m and sorted(arr) == arr:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()
dfs()



