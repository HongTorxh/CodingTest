import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [ i for i in range(1,n+1)]

ans = []
count = 0
for i in range(n):
    count += k - 1
    if count >= len(arr):
        count = count % len(arr) 
    ans.append(str(arr.pop(count)))

print("<",', '.join(ans),">", sep="")