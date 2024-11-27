import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = list(map(int, input().split()))
ans = []
arr.sort()
def back(start):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    for i in range(start, n):
        ans.append(arr[i])
        back(i)
        ans.pop()
back(0)