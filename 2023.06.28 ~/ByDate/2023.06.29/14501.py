import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_day = 0
max_revenue = 0
for i in range(n): 
    day_temp = arr[i][0]
    re_temp = arr[i][1]
    for j in range(day_temp, n):
        day_tmp = j




        