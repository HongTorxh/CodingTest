# 큰 수의 법칙
# M번 더하여 가장 큰 수를 만들 때, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
# ex 2,4,5,4,6이 입력일 때, M이 8이고 K가 3이라 가정
# 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5가 가장 큰 수
# [입력 조건]
# 첫째 줄 : N ( 2 <= N <= 1000), M ( 1 <= M <= 10000), K (1 <= K <= 10000)
# 둘째 줄 : N개의 자연수
# 항상 K는 M보다 작거나 같음
# [출력 조건]
# 첫째 줄에 동빈이의 큰 수의 법칙에 따 더해진 답 출력

# main idea
# sort로 가장 큰 수와 두번째로 큰 수를 가져오기 
# 가장 큰 수를 K번 사용하고, 두번 째로 큰 수를 1번 사용 반복
# M과 같아지면 break
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[-1]
second = arr[-2]
cnt = 0
k_count = 0
answer = 0
while True:
    if cnt == m:
        break
    if k_count == k:
        answer += second
        k_count = 0
        cnt += 1
        continue
    answer += first
    k_count += 1
    cnt += 1
    
print(answer)
    
        