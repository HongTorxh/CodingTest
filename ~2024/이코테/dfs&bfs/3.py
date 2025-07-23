# 음료수 얼려 먹기
# n * m 얼음 틀
# 구멍 뚫린 부분은 0, 칸막이는 1
# 구멍이 뚫려 있는 부분끼리 연결되어 있을 때, 아이스크림의 갯수 구하기
# [입력 조건]
# 첫째 줄 : N, M (1 <= N, M <= 1000)
# 둘째 줄 : N+1번째 줄까지 얼음 틀의 형태
# [출력 조건]
# 아이스크림 갯수 출력
import sys
input = sys.stdin.readline

def dfs(x, y):
    global n, m, arr
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False



n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().strip())))
answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1
            

print(answer)