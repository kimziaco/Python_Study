start_num = int(input())
last_num = int(input())
arr = []

for num in range(start_num, last_num+1):
    cnt = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
        if cnt == 0:
            arr.append(num)

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
