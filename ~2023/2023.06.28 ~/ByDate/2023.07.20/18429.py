import sys
input = sys.stdin.readline

def dfs(depth, t):
    global count
    if(depth == n):
        count +=1
        return ;
    for i in range(n):
        if(check_a[i] == 1 or t+a[i]-k < 0):
            continue
        check_a[i] = 1
        dfs(depth+1, t+a[i]-k)
        check_a[i] = 0



n, k = map(int, input().split())

a = list(map(int, input().split()))

check_a = [0] * n
count = 0

dfs(0, 0)

print(count)