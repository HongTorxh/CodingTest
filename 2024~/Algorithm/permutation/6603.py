import sys, itertools
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]
    for combi in itertools.combinations(arr, 6):
        print(*combi)
    print()

