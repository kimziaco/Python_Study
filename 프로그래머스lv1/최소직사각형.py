a = [[60, 50], [30, 70], [60, 30], [80, 40]]
b = []
c = []

for i in range(len(a)):
    a[i].sort()
    b.append(a[i][0])
    c.append(a[i][1])

print(max(b) * max(c))
