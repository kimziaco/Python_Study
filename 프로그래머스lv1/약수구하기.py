# n = int(input())
# arr = []
# sum = 0

# for i in range(1, n+1):
#     if n % i == 0:
#         arr.append(i)

# for i in arr:
#     sum += i
# print(sum)

# def soultion(n):
#     arr = []
#     sum = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             arr.append(i)
#     for i in arr:
#         sum += i
#     print(sum)

answer = 0
sum =0
    
for i in range(1,n+1):
    if n % i ==0:
        sum+=i
        answer = sum