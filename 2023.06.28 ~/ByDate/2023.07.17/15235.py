    import sys
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))



    result = list (0 for i in range(n))
    count = 1
    for i in range(max(arr)):
        for j in range(n):
            if (arr[j] == 0):
                continue
            arr[j] -= 1
            result[j] = count
            count += 1

    for i in result:
        print(i, end= ' ')