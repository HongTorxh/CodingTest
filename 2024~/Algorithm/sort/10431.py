import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    inp = list(map(int, input().split()))
    idx = inp[0]
    arr = inp[1:]
    result = 0
    result_arr = []
    for student in arr:
        pos = len(result_arr)
        for i in range(len(result_arr)):
            if result_arr[i] > student:
                pos = i
                break
        result_arr.insert(pos, student)
        result += len(result_arr) - (pos + 1)
    print(idx, result)
