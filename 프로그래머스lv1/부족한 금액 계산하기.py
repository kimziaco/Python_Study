price, money, count = map(int, input().split())

answer = sum([price * i for i in range(count+1)])

if answer > money:
    print(answer - money)
else:
    print(-1)
