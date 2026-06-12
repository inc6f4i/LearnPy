for i in range(1,10,1):
    for k in range(1,10,1):
        print(f'{i} * {k} = {i*k}')

for i in range(1,10,1):
    for k in range(1,10,1):
        j = i*k
        print(f'{i} * {k} = {j}')

# 
#가독성 1번, 단 연산이 복잡해지면 2번
#실행속도 1번이 미세하게 빠름, 2번 yeild 컨텍스트 스위칭 오버헤드


#for  i  in  range ( 0 , 3 , 1):
#       for  k  in  range ( 0 , 5 , 1):
#               print("이중 for 문 (i : %d\tk : %d)" % (i , k ))
