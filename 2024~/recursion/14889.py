import sys
import itertools

input = sys.stdin.readline


n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

# n / 2 개의 조합을 
nums = [i for i in range(0, n)]

answer = float('inf')
for start in itertools.combinations(nums, n // 2):
    link = [i for i in nums if i not in start]
    
    start_s = sum(board[i][j] + board[j][i] for i, j in itertools.combinations(start, 2))
    link_s = sum(board[i][j] + board[j][i] for i, j in itertools.combinations(link, 2))

    diff = abs(start_s - link_s)

    answer = min(answer , diff)

print(answer)