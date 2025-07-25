# 2025.07.25 2
# Z
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
result = 0
while n > 0:
    n -= 1
    half = 2 ** n
    # half = 4 -> 16 * 3 result = 48
    # half = 2 -> 4 * 3 result = 60
    # half = 1 -> 1 * 3 result = 63
    if r < half and c < half: #1사분면
        pass
    elif r < half and c>= half: #2사분면
        result += ((half ** 2))
        c -= half
    elif r >= half and c < half: #3사분면
        result += (2 * (half ** 2))
        r -= half
    else: #4사분면
        result += (3 * (half ** 2))
        r -= half
        c -= half
print(result)