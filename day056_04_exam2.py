while True:
    intData = int(input('10~20사이의 숫자입력:'))
    if intData > 20 or 10 > intData :
        print('잘못 입력 다시')
    else :
        print(f'1~{intData} 까지의 합 : {sum(range(1,intData+1))}')
              