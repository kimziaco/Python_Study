# arr1 = [[1, 2], [2, 3]]
# arr2 = [[3, 4], [5, 6]]
# arr3 = []
# for i in range(len(arr1)):
#     arr4 = []
#     for j in range(len(arr1)):
#         arr4.append((arr1[i][j] + arr2[i][j]))
#     arr3.append(arr4)
# print(arr3)

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
tmp = []
for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        tmp = arr1[i][j] + arr2[i][j]
print(tmp)