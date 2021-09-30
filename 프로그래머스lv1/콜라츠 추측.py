n = int(input())
answer = 0

while (n != 1):
    if n % 2 == 0:
        n = n/2
    elif n % 2 == 1:
        n = n*3 + 1
    answer += 1

if answer >= 500:
    print(-1)
else:
    print(answer)

# def solution(num):
#     answer = 0
#     while(num != 1):
#         if num % 2 ==0:
#             num = num/2
#         elif num % 2 ==1:
#             num = num*3 + 1
#         answer += 1
#     if answer >= 500:
#         return -1
#     else: 
#         return answer