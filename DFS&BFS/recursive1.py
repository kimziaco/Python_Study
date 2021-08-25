def recursive_function(i):
    if i ==100:
        return
    print(i,"번째 재귀함수에서", i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, "번째 재귀함수를 종료합니다.")

recursive_function(1)

#재귀함수는 조건에 다다르면 원래 처음값으로 돌아오는가 