# 260604-실습-0-해답
oddSum, evenSum = 0, 0
num = int(input("값 입력 : "))
for i in range(1, num + 1, 1):
    if i % 2 == 0:
        #evenSum = evenSum + i  # 축약형 
        evenSum += i   # For문의 종속문장이 10회 반복되는 동안 i 가 짝수인 경우에만 
                       # 짝수의 합을 누적하는 evenSum 에 i 값을 누적함
    else:
        #oddSum = oddSum + i  # 축약형 
        oddSum += i    # For문의 종속문장이 10회 반복되는 동안 i 가 홀수인 경우에만 
                       # 홀수의 합을 누적하는 oddSum 에 i 값을 누적함
#print("1에서 %d 까지 " % num)
print(f"1에서 {num} 까지 ")
print('홀수의 합 : ', oddSum)
print('짝수의 합 : ', evenSum)