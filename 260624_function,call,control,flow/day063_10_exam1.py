def mySum(ssu1,ssu2):
     result = ssu1 + ssu2
     return result 
def mySub(ssu1,ssu2):
    result = ssu1 - ssu2
    return result
def myDiv(ssu1,ssu2):
    result = ssu1 / ssu2
    return result 
def myMul(ssu1,ssu2):
    result = ssu1 * ssu2
    return result
try:
    su1 = int(input("첫번째 정수를 입력 :"))
    op1 = input('부호를 입력하세요 :')
    su2 = int(input("두번째 정수를 입력 :"))
except ValueError:
    print(f'정수입력')
    exit()

swith_case = {
    "+": mySum(su1,su2),
    "-": mySub(su1,su2),
    "/": myDiv(su1,su2),
    "*": myMul(su1,su2)
}
a = "연산자 오류입니다"
print(f'{su1} {op1} {su2} = {swith_case.get(op1,a)}')

#
