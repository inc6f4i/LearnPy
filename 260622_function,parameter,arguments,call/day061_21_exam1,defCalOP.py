import operator
def calc():
    result =0
    su1, op, su2 = int(input('숫자...')),input('부호...'),int(input('숫자...'))
    op1 = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv
    }
    if op in op1:
        result = op1[op](su1,su2)
        print(su1,op,su2,'=',result)
    else:
        print("사칙연산만 가능합니다.")

while True:
    calc()