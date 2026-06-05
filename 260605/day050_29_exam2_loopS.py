cash = int(input('요금을 투입하세요: '))

while True:
    print('='*7 +'커피 자판기'+'='*7 )
    print('1. 커피(200) 2. 코코아(250) 3. 반환 4. 종료')
    menu = int(input("메뉴를 선택하세요>>>"))
    match menu:
        case 1 :
            if cash >= 200:
                cash -= 200
                print('맛있게드세요')
            else :
                print('요금이부족합니다')
        case 2 :
            if cash >= 250:
                cash -= 250 
                print('맛있게드세요')
            else :
                print('요금이부족합니다')
                 
        case 3 :
            print(f'반환금액{cash}')
            break
              
        case 4 :
            print('프로그램 종료')
            break
              
        case _ :
                print("잘못 입렷하셨습니다.")        







#break 필수 반환금액 산출시