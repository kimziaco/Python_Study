from itertools import combinations
nums = [1, 2, 3, 4]
ans = []
cnt = 0
answer = list(combinations(nums, 3))

for i in range(len(answer)):
    ans.append(sum(answer[i]))

for j in ans:
    for z in range(2, j):
        if j % z == 0:
            cnt += 1
            break
        
print(len(ans) - cnt)
