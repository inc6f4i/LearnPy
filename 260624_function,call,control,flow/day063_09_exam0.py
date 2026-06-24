switch_case = {
    "one" : 1,
    "two" : 2,
    "three" : 3
}
try :
    value = input()
    print('result = ',switch_case)
    print("입력에대한 결과는", switch_case.get(value,"No Data"),"입니다")
except KeyError :
    result = 0
finally :
    print("종료")
#아 이거 value로 되어있어서 헤깔렸네
#키값을 적어놓으면 그에 해당하는 value를 .get하는 것임
#.get()의 파라미터 뒤에꺼는 디폴트값이고, 해당 키가 없으면 디폴트를 리턴함
#즉 No Data가 리턴됨

# try ~ except ~ finally 문법 설명
# 파이썬은 프로그램의 프로그래머가 작성한 소스의 문법적인 오류가 아닌,
# 사용자의 키입력, 데이터베이스 처리, 파일 입출력 등의 과정에서 발생할 수 있는
# 외부 요인과의 소통 중에 발생하는 오류를 대비하기 위하여 
# try, except, finally 구문을 사용합니다.
# try 블록의 수행 중에 오류가 발생하면 except 블록이 수행됩니다. 
# 하지만 try블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않습니다.
# finally 블럭은 무조건 수행하는 영역이며, 생략가능합니다.