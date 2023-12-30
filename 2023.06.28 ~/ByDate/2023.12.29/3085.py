import sys
input = sys.stdin.readline

def check(arr):
    max_temp = 1
    for i in range(n):
        temp = 1
        for j in range(1,n):
            if arr[i][j] == arr[i][j-1]:
                temp +=1
            else:
                temp = 1
            max_temp = max(max_temp, temp)
        temp = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                temp += 1
            else:
                temp = 1
            max_temp = max(max_temp, temp)
    return max_temp
    

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
result = -1 
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            count = check(arr)
            result = max(result, count)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i + 1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            count = check(arr)
            result = max(result, count)
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(result)
