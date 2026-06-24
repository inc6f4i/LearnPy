def add(a,b) : #fall down  , 파이선 컴파일러가 함수만 인식하고 실행하지 않음 // a,b는 매개변수(parameter)
    print('나는 함수입니다') #함수 안에 프린트
    return a+b
#
print("나는 함수를 부르는곳입니다") # 실제 시작점 
num1 = 10
num2 = 20
#a= 10
#b= 20
if num1 == 10 :
    print('나는 if문의 종속문장입니다')
else :
    print('나는 else문의 종속문장입니다')
print('나는 if문의 다음문장입니다')

#c = add(num1,num2) # 함수호출해서 1번라인으로 제어를 넘김jump 

print(    add(num1,num2)    ) # 이 라인 30을 반환함 // num1,num2는 인수 (arugments)
