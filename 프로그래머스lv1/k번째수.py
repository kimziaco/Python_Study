arr = [1,5,2,6,3,7,4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

for command in commands:
    i,j,k = command[0],command[1],command[2]
    slice = arr[i-1:j]
    slice.sort()
    answer.append(slice[k-1])
print(answer)