intData = 2 #정수형 변수 선언
pi = 3.14 # 실수형 변수 선언
flag = False # 블리언형 변수 선언

ch = 'x' #문자열 변수 선언
strData = "사랑해요 파이썬!" #문자열 변수 선언

if flag :
    print('참입니다') # if 조건식의 연산결과가 참일때 실행
else :
    print("거짓입니다") # if 조건식의 연산결과가 거짓일때 실행
#
if intData == 1 :
    print('1입니다') # if 조건식의 연산결과가 참일때 실행
else :
    print("1이 아닙니다") # if 조건식의 연산결과가 거짓일때 실행

"""
이 부분은 여러 줄 주석입니다
여러줄에 걸쳐서 긴설명을 작성할수 있습니다
ㅇ
"""
print(strData[0])
#
setData ={1, 2, 3, 4, 5} # 셋 선언
print(setData)
#
listData = [5+5, 20, 30 , 40] # 인덱스 0~3 
print(listData[0])
#
#dictData = { 0 :False, 1 :True }
dictData = { 1 :5+5, 2 :20, 3 :30, 4 :40  }
print(dictData[1])