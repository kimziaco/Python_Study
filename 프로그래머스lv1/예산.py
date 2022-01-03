import random

d = [2,2,3,3]
budget = 10
ans = 0
cnt = 0
answer = []

# for x in d:
#     ans += x
#     if ans <= budget:
#         cnt += 1
# print(cnt)

# answer = random.sample(d,len(d))
# for x in answer:
#     ans += x
#     if ans <= budget:
#         cnt += 1
# print(cnt)

answer.append(random.sample(d,1))
print(answer)