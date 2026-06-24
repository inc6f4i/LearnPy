def sel_machine():
    sel = 0
    sel = int(input("음료선택\n1.콜라\n2.핫6\n3.포카리\n입력... "))
    if sel == 1 : print('콜라등장')
    elif sel == 2 : print('핫6등장')
    elif sel == 3 : print('포카리등장')
    else : print('만들어 드세요^^')
    
    if sel >= 1 and sel <=3: #인풋으로 숫자받은걸 위에서도 한번 아래에서도 한번
        print("맛있게 드세요 ^^")#실행문은 fallDown인걸 여기서도 다시한번
sel_machine() #이한줄만 주인마님 영역

"""
함수는 위쪽에 선언하니까
주인마님 영역은 아래쪽에 두니까
시작지점이 어딘지 빨리 캐치하는 능력을 기를것
"""