import operator

def cal(su1, op, su2):
    result = 0
    op1 = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
    }
    if op in op1:
        result = op1[op](su1,su2)
    else :
        result = '사칙연산만 가능합니다'
    return result
while True:
    ssu1, oop, ssu2 = int(input('숫자:')), input('부호:'), int(input('숫자:'))
    rresult = cal(ssu1, oop, ssu2)
    print(ssu1,oop,ssu2,'=',rresult)