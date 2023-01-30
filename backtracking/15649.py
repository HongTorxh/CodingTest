import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

def dfs(size):
    if size == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            print("%d append" % i)
            dfs(size + 1)
            temp = arr.pop()
            print("%d pop" % temp)
        print(arr)
dfs(0)