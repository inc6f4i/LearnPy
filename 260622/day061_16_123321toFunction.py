def reverseNum():
    result,temp = 0,0
    result = int(input('숫자만...'))
    while True:
        temp = int(result%10) #끝자리수를 temp에
        result = int(result/10) #result를 다시 10으로 이거이거 123 321로 바꾸는거구만
        print(temp,end='')
        if not result:
            break
print('프로그램시작')
reverseNum()
print('\n프로그램종료')