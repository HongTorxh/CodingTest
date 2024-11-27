import itertools

n = int(input())
arr = list(map(int, input().split()))
answer = float('-inf')
for permu in itertools.permutations(arr, n):
    tmp = 0
    for i in range(n-1):
        tmp += abs(permu[i] - permu[i+1])
    answer = max(answer, tmp)

print(answer)