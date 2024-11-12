import itertools

n = int(input())

nums = [i for i in range(1, n+1)]

for permu in itertools.permutations(nums, n):
    print(" ".join(str(i) for i in permu))
