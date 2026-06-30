#260629_day066_07_.py

remainAttempts = 5
while remainAttempts > 0:
    try : 
        int(input('정수입력:'))
        break
    except :
        remainAttempts -= 1
        print(f'{remainAttempts}회 남음')
        continue