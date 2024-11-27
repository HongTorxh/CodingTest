import sys

input = sys.stdin.readline

n = int(input())

plus = []
minus = []

for _ in range(n):
    input_data = int(input())
    if input_data <= 0:
        minus.append(input_data)
    else:
        plus.append(input_data)

plus.sort()
minus.sort(reverse=True)
result = 0
# 양수와 0 + 음수로 분리해서 입력을 받음
# 양수는 홀수일 경우, 1개까지 진행하다 남은 1개의 경우만 계산
# 짝수일 경우 곱이 큰지 합이 큰지만 고려
idx = 0

def sum_indiv(arr):
    global result
    while len(arr) > 1:
        a = arr.pop()
        b = arr.pop()
        if a * b < a + b:
            result += a + b
        else:
            result += a * b

sum_indiv(plus)
sum_indiv(minus)

if len(plus) > 0:
    result += plus.pop()
if len(minus) > 0:
    result += minus.pop()
print(result)