n = 45
answer = []
result = 0
while(n != 0):
    s = n % 3
    n = n // 3
    answer.append(s)
answer.reverse()

for i in range(len(answer)):
    result += answer[i] * 3**i
print(result)
