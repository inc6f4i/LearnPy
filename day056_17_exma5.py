while True :
    num = int(input("3이상의 홀수의 줄수를 입력하세요 : "))
    while num >= 3 and num%2 != 0:
        center = num // 2
        
        for i in range(0, num):
            for k in range(0, num):
                # 중심점으로부터의 거리가 center 이하인 변수들만 선택
                if abs(i - center) + abs(k - center) <= center:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()       

        num = int(input("0.종료 1.계속 : "))    
    if num == 0 :
        break
    if num == 1 :
        continue
    
    else :
        print('입력한 수가 틀렸습니다.')
