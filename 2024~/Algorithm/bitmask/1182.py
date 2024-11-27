import sys
import itertools
input = sys.stdin.readline

n , s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
for i in range(1, n+1):
    for combi in itertools.combinations(arr, i):
        tmp = sum(combi)
        if tmp == s:
            answer += 1

print(answer)