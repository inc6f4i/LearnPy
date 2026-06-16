ln , flag, st  = 5 , 0, 1
sp =  ln//2
i, j, num = 0, 0, 1
while num:
    try :
        ln = int(input('3 이상의 홀수의 줄수를 입력하세요 : '))    
    except :
        continue #틀린입력 반복대응

    if ln % 2 == 0 or ln < 3:
        print('입력한 수가 틀렸습니다.')
        continue
    flag = 0

    sp = ln//2
    st = 1 
    for i in range (ln): 
        for j in range(sp):  
            print(" ", end="")
        for j in range (st): 
            print("*", end='')
        print()
        if i == (ln//2):
            flag = 1
        if flag == 0: 
            sp -= 1
            st += 2
        else:
            sp += 1
            st -= 2
    while num :
        try :
             num = int(input('0.종료 1.계속 : '))
             break
        except :
            continue
print('프로그램 종료')