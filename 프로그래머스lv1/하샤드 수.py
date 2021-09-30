def solution(x):
    str_x = str(x)
    sum = 0

    for i in str_x:
        sum += i
    if x % sum == 0:
        return True
    return False

# def Harshad(n):
#     return n % sum([int(c) for c in str(n)]) == 0