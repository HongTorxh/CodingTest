import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

time = 0
# False면 R연산
# True면 C연산 
calculation = False
while time <= 100:
    if arr[r-1][c-1] == k:
        print(time)
        break
    if not calculation:
        new_arr = []
        for i in range(len(arr)):
            cnt = {}
            for j in range(len(arr)):
                if arr[i][j] in cnt.keys():
                    cnt[arr[i][j]] += 1
                else:
                    cnt[arr[i][j]] = 1
            sorted_cnt = sorted(cnt.items(), key = lambda x : (x[1], x[0]))
            new_arr.append(sorted_cnt)
        calculation = True
        print(new_arr)
        break
    else:
        calculation = False
    break