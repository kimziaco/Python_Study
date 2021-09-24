def solution(dartResult):
    dart = list(dartResult)  # 한자리씩 list로 생성
    score = []  # 변환한 거 저장해줄 리스트

# 문자열 -> 리스트 처리
    for i in range(len(dart)):
        if dart[i] == '1' and dart[i+1] == '0':  # 10 처리
            score.append('10')
        elif dart[i] == '0' and dart[i-1] == '1':  # 겹치면 pass
            continue
        else:
            score.append(dart[i])  # 나머지는 그냥 하나씩 담기

    # 다트게임 시작
    a = []  # 결과 담을 list

    for s in score:
        if s.isdigit():  # 숫자면 num
            num = int(s)
        elif s.isalpha():  # 숫자 아니면 다트 게임 계산
            if s == 'S':
                num = num ** 1
                a.append(num)  # 각각 저장해줌
            elif s == 'D':
                num = num ** 2
                a.append(num)
            elif s == 'T':
                num = num ** 3
                a.append(num)

		# *, # 처리하기
        if s == '*':  # *이면
            if len(a) >= 2:  # 리스트 2개 이상일 땐 전의 값도 계산해줘야함
                a[-1] = a[-1] * 2
                a[-2] = a[-2] * 2
            else:  # 리스트가 하나값이면 하나만 처리
                a[-1] = a[-1] * 2

        if s == '#':  # 이면 -1
            a[-1] = a[-1] * (-1)

    return sum(a)  # 총합 return


solution('1S2D*3T')
