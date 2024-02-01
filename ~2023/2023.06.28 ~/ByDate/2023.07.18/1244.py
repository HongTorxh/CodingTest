import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

student = int(input())

for i in range(student):
    a, b = map(int, input().split())
    if(a == 1):
        j = 1
        while(b*j<= n):
            if(arr[b*j-1] == 1):
                arr[b*j-1] = 0
            else:
                arr[b*j-1] = 1
            j+=1
    else:
        j = 1
        if(arr[b-1] == 1):
            arr[b-1] = 0
        else:
            arr[b-1] = 1
        while(1):
            if(b-j < 1 or b+j > n):
                break
            if(arr[b-j-1] != arr[b+j-1]):
                break
            if(arr[b-j-1] == 1):
                arr[b-j-1] = 0
            else:
                arr[b-j-1] = 1
            if(arr[b+j-1] == 1):
                arr[b+j-1] = 0
            else:
                arr[b+j-1] = 1
            j+=1

for i in range(1, n+1):
    print(arr[i-1], end = " ")
    if(i % 20 == 0):
        print()
    
        

