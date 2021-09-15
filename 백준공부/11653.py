N = int(input())
arr = []

while N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            arr.append(i)
            N = N // i
            break #break가 들어가면서 for문에 대한 반복문이 나가면서 while로 가는것임 결국 N은 1이될때까지 나누어짐
            

for i in arr:
    print(i)
