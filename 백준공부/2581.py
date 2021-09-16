N = int(input())
M = int(input())
sosu = []

for i in range(N, M+1):
    cnt = 0
    if i == 1:
        pass
    for j in range(2, N):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        sosu.append(i)

if len(sosu) == 0:
    print(-1)
else:
    print(int(sum((sosu))))
    print(min(sosu))
