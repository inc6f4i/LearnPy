def say_myself(name, age, man=True):
    print('나의이름은 %s입니다'%name)
    print('나이는 %d살입니다'%age)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
#
say_myself('아무개',27)
say_myself('아무개',27,True)
say_myself('아무2',25,False)