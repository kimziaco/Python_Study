# lottos = [45, 4, 35, 20, 3, 9]
# win_nums = [20, 9, 3, 45, 4, 35]
# answer = []
# lowcnt = 0
# highcnt = 0

# for i in range(len(lottos)):
#     for j in range(len(win_nums)):
#         if lottos[i] == win_nums[j]:
#             lowcnt += 1
#             highcnt = lowcnt

# for i in lottos:
#     if i == 0:
#         highcnt += 1

# if highcnt == 6:
#     answer.append(1)
# elif highcnt == 5:
#     answer.append(2)
# elif highcnt == 4:
#     answer.append(3)
# elif highcnt == 3:
#     answer.append(4)
# elif highcnt == 2:
#     answer.append(5)
# else:
#     answer.append(6)

# if lowcnt == 6:
#     answer.append(1)
# elif lowcnt == 5:
#     answer.append(2)
# elif lowcnt == 4:
#     answer.append(3)
# elif lowcnt == 3:
#     answer.append(4)
# elif lowcnt == 2:
#     answer.append(5)
# else:
#     answer.append(6)

# print(answer)

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = []

rank = [6, 6, 5, 4, 3, 2, 1]

cnt_0 = lottos.count(0)
ans = 0

for x in win_nums:
    if x in lottos:
        ans += 1
print(rank[cnt_0 + ans - 1], rank[ans-1])

# 1개일치랑 0개가 일치하는 경우는 둘다 6등이므로 rank를 6을 두번 넣어주는것이 옳다.
