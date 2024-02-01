# import sys
# input = sys.stdin.readline

# s = input()

# arr = [] # 2진수 저장 배열


# for i in s[:-2]: #마지막 요소가 \n이기 때문에 제외
#     temp = ord(i) #문자를 ascii 코드로
    
#     if(temp > 64 and temp < 91): #대문자
#         temp = temp - 65
#     elif(temp > 96 and temp < 123): # 소문자
#         temp = temp - 71
#     elif(temp > 47 and temp < 58):
#         temp = temp + 4
#     elif(temp == 42): # ASCII : +
#         temp = 62
#     elif(temp == 47): # ASCII : /
#         temp = 63

#     count = 6
#     tmp = []
#     while(count != 0):
#         b = temp % 2
#         tmp.append(b)
#         temp = temp // 2
#         count -= 1
#     tmp.reverse()
#     arr.extend(tmp)

# # if(len(arr) % 8 != 0):
# #     remainder = 8 - (len(arr) % 8)
# #     for i in range(0, remainder):
# #         arr.append(0)

# sum = 0
# count = 7
# result = []
# # print(result_arr)
# for i in arr:
#     sum += (i * (2 ** (count)))
#     if (count == 0):
#         if(sum > 127):
#             count = 7
#             sum = 0
#             continue
#         count = 7
#         result.append(sum)
#         sum = 0
#         continue
#     count -= 1

# for i in result:
#     print(chr(i), end="")

# print("\n")
import base64
print (str( base64.b64decode(input().encode('ascii') ))[2:-1] )