import sys
input = sys.stdin.readline

MAX = 1000000
arr = [True] * (MAX + 1)
arr[0], arr[1] = False, False

for i in range(3, int((MAX+1) ** 0.5), 2):
    j = 2
    while (i*j) <= MAX:
        arr[i*j] = False
        j += 1

while True:
    n = int(input())
    if n == 0:
        break
    flag = 0
    for i in range(3, n, 2):
        if arr[i] and arr[n - i]:
            print("{0} = {1} + {2}".format(n, i, n-i))
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")
    