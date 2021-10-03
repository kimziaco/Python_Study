a, b = map(int, input().split())
answer = []

if a > b:
    a, b = b, a
    for i in range(a, b+1):
        answer.append(i)
else:
    for i in range(a, b+1):
        answer.append(i)

print(sum(answer))


def solution(a, b):
    if a>b: a,b = b,a
    return sum(range(a,b+1))