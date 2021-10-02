# n = int(input())
# answer = []


# for i in range(1, n+1):
#     if n % i == 0:
#         answer.append(i)
# print(sum(answer))

def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])


def soulutin2(n):
    return sum([i for i in range(1, n/2+1) if n % i ==0])
