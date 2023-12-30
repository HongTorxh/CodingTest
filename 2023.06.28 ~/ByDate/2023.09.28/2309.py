import sys
input = sys.stdin.readline

def dfs(depth, start):
    if depth == 7:
        if sum(result_arr) == 100:
            for j in sorted(result_arr):
                print(j)
            exit()
        else:
            return
    for i in range(start, len(arr)):
        result_arr.append(arr[i])
        dfs(depth+1, i + 1)
        result_arr.pop()


arr = list(int(input()) for _ in range(9))
result_arr = []

dfs(0,0)