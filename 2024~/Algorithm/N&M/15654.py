import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = list(map(int, input().split()))
ans = []
arr.sort()
def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    for i in arr:
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()
back()