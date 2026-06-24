#won = 10  # 매일 예금하는 금액이 저장되는 변수
#sum = 0   # 저축액 (매일 예금한 금액을 더한것) 저장되는 변수
#for day in range(1, 31):
#    sum += won  # 매일 예금하는 금액을 모은 예금총액(저축총금액)을 누적함
#    won *= 2    # 매일 예금하는 금액(은행에 입금하는 돈)을 계산함
#    if day%10 == 0 and day < 30: # 10일,20일까지의 예금총액을 출력하기 위한 조건문 --->서비스코드임
#        print(day,"일까지 예금총액 :", format(sum,','),'원' ) 
#print("한달 동안 예금총액 :", format(sum,','),'원')


#리스트 만들어서 해설과 비슷한 효과 내기
a = [10*2**i for i in range(30)]
sum = sum(a)
day = 10
sum1 = a[ :day]


print(day,"일까지 예금총액 :", format(sum1,','),'원' ) 
print("한달 동안 예금총액 :", format(sum,','),'원')