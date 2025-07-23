import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
# cctv 확인
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctvs.append((i, j, arr[i][j]))
cctv_1 = [(-1, 0), (1, 0), (0, 1), (0, -1)]
cctv_2 = [[(-1, 0), (1,0)], [(0,1), (0, -1)]]
cctv_3 = [[(-1,0), (0,1)], [(0,1), (1,0)], [(1,0),(0,-1)], [(-1, 0), (0, -1)]]
cctv_4 = [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]]
# cctv 번호로 올림차순
cctvs.sort(key = lambda x : x[2])

# 1~5는 cctv, 6은 벽
# 5~1 순으로 cctv별 탐색 후 사각 지대 최솟값

def check(x, y, cctv):
    if cctv == 5:
        for i in range(x, -1, -1):
            if arr[i][y] == 6:
                break
            elif 0 < arr[i][y] < 6:
                continue
            arr[i][y] = '#'
        for i in range(x, n):
            if arr[i][y] == 6:
                break
            elif 0 < arr[i][y] < 6:
                continue
            arr[i][y] = '#'
        for i in range(y, -1, -1):
            if arr[x][i] == 6:
                break
            elif 0 < arr[x][i] < 6:
                continue
            arr[x][i] = '#'
        for i in range(y, m):
            if arr[x][i] == 6:
                break
            elif 0 < arr[x][i] < 6:
                continue
            arr[x][i] = '#'
    elif cctv == 4:
        for c in cctv_4:
            
            

while cctvs:
    x, y, cctv = cctvs.pop()
    check(x, y, cctv)
    break

for i in arr:
    print(i)
