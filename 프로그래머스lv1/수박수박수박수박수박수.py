def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 ==0:
            answer += '수'
        else:
            answer += '박'
    return answer

def solution2(n):
    return ('수박'* n)[:n] 
# '수박'을 n번만큼 반복하는데 n번째에서 슬라이스해주기