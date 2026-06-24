# day063_12.py
def mySum(firstNum,secondNum):
    return firstNum+secondNum
def mySub(firstNum,secondNum):
    return firstNum-secondNum
def myDiv(firstNum,secondNum):
    return firstNum/secondNum
def myMul(firstNum,secondNum):
    return firstNum*secondNum
try:
    su1 = int(input("숫자 :"))
    op1 = input('부호 :')
    su2 = int(input("숫자 :"))
    if op1 == '+':
        result = mySum(su1,su2)
    elif op1 == '-':
        result = mySub(su1,su2)
    elif op1 == '/':
        result = myDiv(su1,su2)
    elif op1 == '*':
        result = myMul(su1,su2)
    else:
        print("연산자가 오류입니다.")
        exit()
    print(su1, op1, su2,'=',result)
except ValueError:
    print(f'정수입력')
    exit()
except ZeroDivisionError:
    print(f'0으로 나눌수 없습니다')
    exit()

    