import math


arry = [True for i in range(10001)]


for i in range(2, int(math.sqrt(10000)+1)):
    if arry[i] == True:
        j = 2
        while i * j <= 10000:
            arry[i*j] = False
            j += 1


for i in range(int(input())):
    n = int(input())
    a = n//2
    b = a
    while a >= 2:
        if arry[a] and arry[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
