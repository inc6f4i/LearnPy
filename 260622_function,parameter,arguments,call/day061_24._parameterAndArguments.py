#함수 정의 및 호출, 반환의 가장 전형적인 사례
def cal(su1, op, su2): #매 개 변 수
    result22 = 0
    result22 = su1 + su2
    print('cal실행')
    return result22

ssu1, oop, ssu2 = int(input('숫자...')), input('부호...'), int(input('숫자...'))
result = cal(ssu1, oop, ssu2) # 인 수    매 개 변 수와 다르게
print(ssu1,'+',ssu2,'=',result) #전역변수에 할당하려면 return을통해 Global 안쓰고 이렇게 씀
print('다음 문장 실행')


#호출곳에 다시 return을 하는데 옆에 들고갈게 있으면 그걸 들고감
#단순 return만이면 None
#가장 전형적인 사용사례