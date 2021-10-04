# def solution(s):
#     answer=[]

#     for i in range(len(s)):
#         if i % 2==0:
#             answer.append(s[i].upper())
#         else:
#             answer.append(s[i].lower())

#     return "".join(answer)


# s = "try hello world"
# answer = s.split(' ')
# arr = []
# for i in range(len(answer)):
#     for j in range(len(answer[i])):
#         if j % 2 == 0:
#             arr.append(answer[i][j].upper())
#         else:
#             arr.append(answer[i][j].lower())
# print(" ".join(arr))

# s = "try hello world"

# answer = s.split(' ')
# arr = []
# for i in range(len(answer)):
#     str = ''
#     for j in range(len(answer[i])):
#         if j % 2 == 0:
#             str += answer[i][j].upper()
#         else:
#             str += answer[i][j].lower()
#     arr.append(str)
# print(" ".join(arr))
s = "try hello world"
answer = s.split(' ')
arr = []
for i in range(len(answer)):
    for j in range(len(answer[i])):
        if j % 2 == 0:
            arr.append(answer[i][j].upper())
        else:
            arr.append(answer[i][j].lower())
    arr.append(" ")
print("".join(arr))
