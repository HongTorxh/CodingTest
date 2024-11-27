import sys
import itertools

input = sys.stdin.readline


n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

answer = float('inf')

visited = [0] * n

def calculate(arr):
    score = 0
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            score += board[arr[i]][arr[j]] + board[arr[j]][arr[i]]
    
    return score

def backtracking(dep, start):
    global answer
    
    if dep > 0 and dep < n:
        start_t = [i for i in range(n) if visited[i]]
        link_t = [i for i in range(n) if not visited[i]]

        start_s = calculate(start_t)
        link_s = calculate(link_t)

        answer = min(answer, abs(start_s - link_s))

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            backtracking(dep + 1, i + 1)
            visited[i] = False

backtracking(0, 0)

print(answer)