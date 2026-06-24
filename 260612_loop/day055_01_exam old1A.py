print(10*(2**30-1))

print(sum(10*2**i for i in range(30)))

cash = 10; credit = 0

for i in range(1,31):
    if i == 1 :
        credit = cash
    else :
        cash *= 2
        credit += cash 

print(i[10])
print(f'한달간 예금 총액: \033[1;3m{credit: ,}원\033[0m')
print(f'한달간 예금 총액: \033[1;3m{format(credit, " ,")}원\033[0m')
#260610-실습-1 해답
#
won = 10  # 매일 예금하는 금액이 저장되는 변수
sum = 0   # 저축액 (매일 예금한 금액을 더한것) 저장되는 변수
for day in range(1, 31):
    sum += won  # 매일 예금하는 금액을 모은 예금총액(저축총금액)을 누적함
    won *= 2    # 매일 예금하는 금액(은행에 입금하는 돈)을 계산함
    if day%10 == 0 and day < 30: # 10일,20일까지의 예금총액을 출력하기 위한 조건문 --->서비스코드임
        print(day,"일까지 예금총액 :", format(sum,','),'원' ) 
print("한달 동안 예금총액 :", format(sum,','),'원')