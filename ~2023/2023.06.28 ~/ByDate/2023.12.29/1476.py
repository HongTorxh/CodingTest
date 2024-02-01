import sys
input = sys.stdin.readline

e, s, m = map(int,input().split())

result = 1
count_e = 1
count_s = 1
count_m = 1
while True:
    if e == count_e and s == count_s and m == count_m:
        print(result)
        break
    result += 1
    count_e += 1
    count_s += 1
    count_m += 1
    if count_e > 15:
        count_e = 1
    if count_s > 28:
        count_s = 1
    if count_m > 19:
        count_m = 1
