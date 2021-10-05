n = int(input())
answer = 0
for i in str(n):
    answer += int(i)


def solution1(n):
    return sum([int(i) for i in str(n)])


def solution2(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n = n//10
    return answer


def solution3(n):
    if n < 10:
        return n
    return (n % 10) + solution3(n // 10)
