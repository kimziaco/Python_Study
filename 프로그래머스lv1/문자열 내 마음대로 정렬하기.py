strings = ["abce", "abcd", "cdx"]
n = 2
answer = []

for i in strings:
    answer.append(i[n] + i)

answer.sort()

new = []

for j in answer:
    new.append(j[1:])

print(new)
