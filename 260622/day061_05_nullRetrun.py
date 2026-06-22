def add(a,b):   
    print('%d와 %d의 합은 %d입니다'%(a, b, a+b))
a = add(3 , 4) #리턴문이 없는경우 호출된 함수가 되돌려줄 값이 없음, 함수는 수행된뒤 None이 할당됨
print (a)
#앞서 한 예제
if a == 0 :
    print('나는 if문의 종속문장입니다')
else :
    print('나는 else문의 종속문장입니다') #a = None이기 때문에 else가 실행됨
print('나는 if문의 다음문장입니다')