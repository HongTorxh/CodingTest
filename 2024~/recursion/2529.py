import sys

input = sys.stdin.readline

k = int(input())
arr = list(map(str, input().rstrip().split()))
nums = [0] * 9

min_num = "9876543210"
max_num = "0123456789"

def is_valid(a, b, sign):
    if sign == '<':
        return a < b
    elif sign == '>':
        return a > b
    return False


def backtracking(depth, num):
    global min_num, max_num

    if depth == k + 1:
        min_num = min(min_num, num)
        max_num = max(max_num, num)
        return

    for i in range(10):
        if str(i) not in num:
            if depth == 0 or is_valid(num[-1], str(i), arr[depth - 1]):
                backtracking(depth + 1, num + str(i))

backtracking(0, "")

print(max_num)
print(min_num)


