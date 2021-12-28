arr = list(map(int, input().split()))
answer = []
divisor = int(input())

for i in arr:
    if i % divisor == 0:
       answer.append(i)
       answer.sort()
    if len(answer) == 0:
        answer.append(-1)
print(answer)


# return sorted([x for x in arr if x % divisor == 0] or [-1])
