import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]

print(arr)