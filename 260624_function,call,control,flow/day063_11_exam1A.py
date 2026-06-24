# 260624-실습-1-해답
# 이 해답코드를 드래그한 후에 복사, 붙여넣기 하면 에러가 발생할 수 있습니다.
# 게시판 프로그램에서 이상한 코드가 붙어서 그런 것으로 추정됩니다.
# 따라서, 에러가 발생하는 학습자는 복,붙 하지 말고 눈으로 보는 내용을 
# 그대로 타이핑 하시기 바랍니다.
#
def mySum(firstNum,secondNum):   # 덧셈연산 함수
    return firstNum + secondNum  # 덧셈연산 결과를 반환함
def mySub(firstNum,secondNum):   # 뺄셈연산 함수
    return firstNum - secondNum  # 뺄셈연산 결과를 반환함
def myMul(firstNum,secondNum):   # 곱셈연산 함수
    return firstNum * secondNum  # 곱셈연산 결과를 반환함
def myDiv(firstNum,secondNum):   # 나눗셈연산 함수
    return firstNum / secondNum  # 나눗셈연산 결과를 반환함
#
num1 = int(input("첫번째 정수를 입력 : "))
oop = input("부호를 입력하세요 : ")
num2 = int(input("두번째 정수를 입력 : "))
#
# expr 딕셔너리를 만듬
# expr 딕셔너리는 연산자를 키로 갖고 함수호출문장을
# 값으로 가진 쌍들이 4쌍 존재함
expr={"+" : mySum(num1,num2), # 딕셔너리 쌍 4개
      "-" : mySub(num1,num2), # 키 , 값
      "*" : myMul(num1,num2), # expr딕셔너리에서.get(맞는키값을 찾아서) 밸류를 가져오는데
      "/" : myDiv(num1,num2) # 밸류가 함수임
}
"""
키에 대응하는 밸류가 함수인게 킥, 실행문을 집어넣어도 ㅇㅋ,
이 소스코드를 관용어구로 기억해놔야할 정도
고급스런 코딩에 사용
"""
#
# expr 딕셔너리를 get함수를 이용하여 사용자가 input
# 을 이용하여 입력한 연산자에 대응하는 결과값을 result에 할당함
#
result = expr.get(oop,'연산자가 오류입니다.')
#
print(num1,oop,num2,'=',result) # result를 출력함


# 난이도가 좀 있는걸로 봐서 ㅇ
"""
내가 이거 보고 개선할점
return에 실행문을 넣어 반환함(훨씬 간편한 코딩)

"""
#return