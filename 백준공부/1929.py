import math

M, N = map(int, input().split())

arry = [True for i in range(N+1)]

for i in range(2, int(math.sqrt(N))+1):
    if arry[i] == True:
        j = 2
        while i*j <= N:
            arry[i*j] = False
            j += 1

for i in range(M, N+1):
    if i != 1:
        if arry[i]:
            print(i)
