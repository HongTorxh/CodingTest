import sys
input = sys.stdin.readline

while(1):
    try:
        n = int(input())
    except:
        break
    count = 1
    m = 1
    while(1):
        if m % n == 0:
            print(count)
            break
        m = m * 10 + 1
        count = count + 1

