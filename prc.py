n = 12345

a = [int(i) for i in str(n)]
print(sorted(a,reverse=True))

def solution(n):
    return [int(i) for i in str(n)][::-1]
