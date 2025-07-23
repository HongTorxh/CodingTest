import sys
input = sys.stdin.readline

n = int(input())
arr = []
KBS_1 = 0
KBS_2 = 0
for i in range(n):
    tmp = input().strip()
    if tmp == "KBS1":
        KBS_1 = i
    elif tmp == "KBS2":
        KBS_2 = i
    arr.append(tmp)

# 방법의 길이가 500보다 작아야하는데, N의 최댓값이 100이기에 최대로 해도 400번이 최대임
result = []
for i in range(0, KBS_1):
    result.append(1)
for i in range(0, KBS_1):
    result.append(4)
if KBS_2 < KBS_1:
    KBS_2 += 1
for i in range(0, KBS_2):
    result.append(1)
for i in range(1, KBS_2):
    result.append(4)

print("".join(str(i) for i in result))