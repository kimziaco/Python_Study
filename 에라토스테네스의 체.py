import math

n = int(input())

arry = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if arry[i] == True:
        j = 2
        while i*j <= n:
            arry[i*j] = False
            j += 1

for i in range(2, n+1):
    if arry[i]:
        print(i, end=' ')
