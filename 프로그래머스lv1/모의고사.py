answers = [1, 3, 2, 4, 2]

num1 = [1, 2, 3, 4, 5]
num2 = [2, 1, 2, 3, 2, 4, 2]
num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
correct = []
cnt = [0, 0, 0]

for i in range(len(answers)):
    if answers[i] == num1[i % len(num1)]:
        cnt[0] += 1
    if answers[i] == num2[i % len(num2)]:
        cnt[1] += 1
    if answers[i] == num3[i % len(num3)]:
        cnt[2] += 1

k = max(cnt)

for i in range(len(cnt)):
    if k == cnt[i]:
        correct.append(i+1)
        
print(sorted(correct))