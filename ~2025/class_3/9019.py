# 2023.07.28 4
# DSLR
import sys
from collections import deque
input = sys.stdin.readline
# n의 네 자릿수 : n = ((d1 * 10 + d2) * 10 + d3) * 10 + d4
# D : n을 2배로 ; 9999보다 큰 경우 10000으로 나눈 나머지
# S : n-1 ; if n == 0 : 9999
# L : 왼편 회전 ; d2, d3, d4, d1
# R : 오른편 회전 ; d4, d1, d2, d3
t = int(input()) # 테스트 케이스

def bfs(start, end):
    dq = deque([start])
    visited = [False] * 10000
    visited[start] = True
    result = [""] * 10000
    while dq:
        x = dq.popleft()
        if x == end:
            return result[x]
        for c, cmd in [('D', command_D), ('S', command_S), ('L', command_L), ('R', command_R)]:
            nx = cmd(x)
            if not visited[nx]:
                visited[nx] = True
                dq.append(nx)
                result[nx] = result[x] + c
        # D
        # nx = (x * 2) % 10000
        # if not visited[nx]:
        #     visited[nx] = True
        #     result[nx] = result[x] + 'D'
        #     dq.append(nx)
        # # S
        # nx = (x -1) if nx != 0 else 9999
        # if not visited[nx]:
        #     visited[nx] = True
        #     result[nx] = result[x] + 'S'
        #     dq.append(nx)
        # # L
        
def command_D(num):
    return (num * 2) % 10000
def command_S(num):
    return num-1 if num != 0 else 9999
def command_L(num):
    return (num  % 1000) * 10 + (num // 1000)

def command_R(num):
    return (num % 10) * 1000 + (num // 10)

for _ in range(t):
    a, b = map(int, input().split()) #a는 초기, b는 최종
    print(bfs(a, b))

