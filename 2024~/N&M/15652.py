import sys
input = sys.stdin.readline

n, m = map(int,input().split())
ans = []

def back(start):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    for i in range(start, n+1):
        ans.append(i)
        back(i)
        ans.pop()
back(1)