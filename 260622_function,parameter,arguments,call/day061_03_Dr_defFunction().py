def add(a,b):   # 이문장에서 a 와 b는 매개변수라고 불리는 변수입니다. 
                # 함수의 입력값을 저장하는 변수입니다.
    print('나는 함수입니다.')
    return a + b  
#
print("나는 함수를 부르는 곳입니다.")
num1 = 10
num2 = 20
#a = 10
#b = 20
if num1 == 10 :
    print('나는 if 문의 종속문장입니다.')
else:
    print('나는 else문의 종속문장입니다.')
print('나는 if문의 다음문장입니다.')
#c = add(a , b )   # 이 문장에서 a , b는 인수인데 위의 함수 정의 부분의 매개변수와
                # 변수명을 동일하게 함으로써 사용자를 혼란하게할 수 있기에 자제하여야 한다.
#c = add(num1, num2)
#print(c)
print(  add(num1, num2)  )  # 이 문장에서 num1과 num2는 인수라고 불리는 값입니다.