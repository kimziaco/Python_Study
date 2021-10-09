# n = int(input())
# answer = 0
# for i in range(2, n+1):
#     cnt = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             cnt += 1
#     if cnt == 2:
#         answer += 1

# print(answer)


def solution1(n):
    answer = 0
    for i in range(2, n+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 2:
            answer += 1
    return answer

# 시간효율성이 좋지 않은 코드임

import math
def solution2(n):
    answer = 0
    
    arry = [True for i in range(n+1)]
    
    for i in range(2, int(math.sqrt(n))+1):
        if arry[i] == True:
            j = 2
            while i * j <=n:
                arry[i*j] = False
                j +=1
    answer = arry.count(True)-2
    return answer

def solution3(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
