#260622일차-실습-2-해답-ver1 
#함수 호출에 인수가 있고 반환도 하는 사칙연산
def cal(su1, op, su2):
    result = 0
    if op=='+':
        result = su1+su2
    elif op=='-':
        result=su1-su2
    elif op=='*':
        result=su1*su2
    elif op=='/':
        result=su1/su2        #여기까지 하나라도 걸리면
    else:
        pass
    return result         #result를 호출한 곳에 보냄

su1,op,su2 = int(input("숫자:")),input("부호 :"),int(input("숫자:"))
result=cal(su1,op,su2)
if op == '+' or op == '-' or op == '*' or op == '/' : 
    print(su1,op,su2,'=',result)
else:
    print("사칙연산만 가능합니다.")