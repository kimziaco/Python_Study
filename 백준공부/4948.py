import math

n = int(input())
arry = [True for i in range(2*n+1)]
cnt = 0

for i in range(2, int(math.sqrt(2*n)+1)):
    if arry[i] == True:
        j = 2
        while i*j <= 2*n:
            arry[i*j] = False
            j += 1

for i in range(n+1, 2*n+1):
    if arry[i]:
        cnt += 1
print(cnt)
