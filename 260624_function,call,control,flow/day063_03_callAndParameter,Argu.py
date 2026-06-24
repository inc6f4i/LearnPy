def myType(su):
    if type(su) == int:
        return str(su) + ": 정수(int)형태입니다"
    elif type(su) == str:
        return su + ": 문자(str)형태입니다."
    elif type(su) == float:
        return str(su) + "실수입니다"
    else:
        return "어떤것인지 모르겠습니다"
num1 = input('수입력')
num2 = int(input('수입력'))
num3 = float(input('수입력플롯'))

print(myType(num1))
#print(myType(num2))
#print(myType(num3))

