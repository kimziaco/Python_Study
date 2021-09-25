def solution(arr):
    sum = 0
    count = 0
    for i in arr:
        sum += i
        count = len(arr)
    return sum / count

# 로 짰지만, 그냥 간단하게한줄코딩하면
# return sum(arr)/len(arr)로 하면된다..