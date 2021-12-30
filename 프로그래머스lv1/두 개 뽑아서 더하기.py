numbers = [2, 1, 3, 4, 1]
answer = set()

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        answer.add(numbers[i]+numbers[j])
answer = list(answer)
answer.sort()
print(answer)


# def solution(numbers):
#     answer = set()
#     for i in range(len(numbers)):
#         for j in range(i+1,len(numbers)):
#             answer.add(numbers[i]+numbers[j])
#     answer = list(answer)
#     answer.sort()
#     return answer