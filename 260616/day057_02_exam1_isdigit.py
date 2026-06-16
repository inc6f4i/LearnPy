#260615-실습-5-해답
ln = 5; flag = 0; sp = ln//2; st = 1;
i, j, num = 0, 0, 1;
while num:

    x = input('3 이상의 홀수의 줄수를 입력하세요 : ')
    if not x.isdigit():
        continue
        
    ln = int(x)


    if ln % 2 == 0 or ln < 3:   # 3 이상의 짝수가 아니면 다시입력하도록 함
        print('입력한 수가 틀렸습니다.')
        continue
    flag = 0    # 플래그를 의미하는 변수임. 특정 시점에 다다르면
                   # 반복에 사용한 증감의 규칙을 변경하는데 사용됨
                   # 마라톤의 반환점에 비유할 수 있음
    sp = ln//2  # 공백을 찍는데 사용하는 반복문의 변수임
    st = 1       # 별을 찍는데 사용하는 반복문의 변수임
    for i in range (ln):        # 입력한 숫자(라인)를 사용하는 반복문
        for j in range(sp):    # 공백을 출력하는 반복문
            print(" ", end="")
        for j in range (st):   # 별을 출력하는 반복문
            print("*", end='')
        print()
        if i == (ln//2):        # 입력한 수의 반을 체크하여 flag를 변경함
            flag = 1
        if flag == 0:           # flag의 값에 따라 반복문의 증감 규칙을 다르게함
            sp -= 1
            st += 2
        else:
            sp += 1
            st -= 2
    y = input('0.종료 1.계속 : ')
    while y:
        if not y.isdigit():
        
        else 
    num = int(y)
print('프로그램 종료')