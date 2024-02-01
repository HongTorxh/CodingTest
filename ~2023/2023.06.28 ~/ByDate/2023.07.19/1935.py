import sys
input = sys.stdin.readline

n = int(input())

string = input()

a = {}
for i in range(n):
    temp = int(input())
    a[chr(i+65)] = temp

stack = []
for i in range(len(string)-1):
    if(string[i] == '+'):
        temp_1 = stack.pop()
        temp_2 = stack.pop()
        stack.append(temp_1 + temp_2)
    elif(string[i] == '-'):
        temp_1 = stack.pop()
        temp_2 = stack.pop()
        stack.append(temp_2 - temp_1)
    elif(string[i] == '*'):
        temp_1 = stack.pop()
        temp_2 = stack.pop()
        stack.append(temp_2 * temp_1)
    elif(string[i] == '/'):
        temp_1 = stack.pop()
        temp_2 = stack.pop()
        stack.append(temp_2 / temp_1)
    else:
        stack.append(a[string[i]])

print("{:0.2f}".format(stack[0]))