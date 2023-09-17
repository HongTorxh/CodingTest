import sys
input = sys.stdin.readline

def dfs(depth, result, plus, minus, mul, div):
    global res_max, res_min
    if depth == n:
        res_max = max(result, res_max)
        res_min = min(result, res_min)
        return
    if plus:
        dfs(depth+1, result + a[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth+1, result - a[depth], plus, minus-1, mul, div)
    if mul:
        dfs(depth+1, result * a[depth], plus, minus, mul-1, div)
    if div:
        if result > 0:
            dfs(depth+1, result // a[depth], plus, minus, mul, div-1)
        else:
            result = -result
            result = result // a[depth]
            result = -result
            dfs(depth+1, result, plus, minus, mul, div-1)


n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

res_max = -1e10
res_min = 1e10


dfs(1, a[0], plus, minus, mul, div)
print(res_max)
print(res_min)