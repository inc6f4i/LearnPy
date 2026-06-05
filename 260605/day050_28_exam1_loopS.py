# 260605-실습-1-해답
# 이 문제는 단순한 for문의 구현의 목적이 아닙니다. 
# 반복을 설계할 때, for문의 종속문장 내부를 개별 작업(if~else)을 구분한 후에,
# 각각의 개별 작업에서 또다시 세부적인 개별작업(3항연산자)으로 구분하는 것이 핵심입니다.
oddSum, evenSum = 0, 0
num = int(input("값 입력 : "))
st_odd ='홀수 : '
st_even ='짝수 : '
for i in range(num, 0, -1):
    if i % 2 == 0:
        st_even += (str(i) + ' ') if i == 2 else (str(i) + ', ')
        evenSum += i   # For문의 종속문장이 10회 반복되는 동안 i 가 짝수인 경우에만 
                       # 짝수의 합을 누적하는 evenSum 에 i 값을 누적함
    else:
        st_odd += (str(i) + ' ') if i == 1 else (str(i) + ', ')
        oddSum += i    # For문의 종속문장이 10회 반복되는 동안 i 가 홀수인 경우에만 
                       # 홀수의 합을 누적하는 oddSum 에 i 값을 누적함
print("-"*50)
print(st_odd,' 홀수의 합 : ', oddSum)
print("-"*50)
print(st_even,' 짝수의 합 : ', evenSum)
print("-"*50)
print("%d 에서 1 까지의 합 : %d" % (num, oddSum + evenSum))

print (list(range(num, 0, -1)))