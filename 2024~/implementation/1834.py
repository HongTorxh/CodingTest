import sys
input = sys.stdin.readline

n = int(input())

answer = 0
idx = 1
while idx < n:
    num = idx * n + idx
    idx += 1
    answer += num

print(answer)