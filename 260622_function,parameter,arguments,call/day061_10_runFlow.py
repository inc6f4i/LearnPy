num1 = 10 #가장 먼저 실행하는 falldown
num2 = 20
def say_myself(name, age, man=True): #수행하지 않음
    print('나의이름은 %s입니다'%name)
    print('나이는 %d살입니다'%age)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
    print()
#
say_myself('아무개',27) #인자들을 함수 파라미터에 할당, man에대한 인자가 없어서 초기값 true가 할당
say_myself('아무2',25,False)
print(num1 + num2)

# 수행방식1,2 12,3,4,5,6,7 13,3,4,5,8,9,10, 14 종료