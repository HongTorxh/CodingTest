# 숫자 카드 게임
# 1. N * M 배열
# 2. 행을 선택
# 3. 해당 행의 가장 숫자가 낮은 카드를 뽑기
# 4. 가장 높은 숫자 카드를 뽑아야 함
# [입력 조건]
# 첫째 줄 : N, M (1 <= N, M <= 100)
# 둘째 줄 : N개의 수
# [출력 조건]
# 게임의 룰에 맞게 선택한 카드에 적힌 숫자 출력

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = -float('inf')
for i in arr:
    min_v = min(i)
    answer = max(answer, min_v)
    

print(answer)