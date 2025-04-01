import sys
input = sys.stdin.readline

n = int(input())


quo = n // 3
rem = n % 3
# SK
if quo % 2 == 0:
    # CY
    if rem == 0:
        print("CY")
    elif rem == 1:
        print("SK")
    else:
        print("CY")
else:
    if rem == 0:
        print("SK")
    elif rem == 1:
        print("CY")
    else:
        print("SK")
