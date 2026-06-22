#260622일차-실습-2-해답-ver2
#함수 호출에 인수가 있고 반환도 하는 사칙연산
def cal(su1, op, su2):
    #result = 0
    #if op=='+':
    #    result = su1+su2
    #elif op=='-':
    #    result=su1-su2
    #elif op=='*':
    #    result=su1*su2
    #elif op=='/':
    #    result=su1/su2
    #else:
    #    pass
    return eval(f"{su1} {op} {su2}")  # eval함수는 보안측면에서 권장하지 않음
    # https://www.google.com/search?q=eval%28%29+%ED%8C%8C%EC%9D%B4%EC%8D%AC&oq=%E3%84%B7%E3%85%8D%EB%AF%B8%28%29&gs_lcrp=EgZjaHJvbWUqDAgCEAAYFBiHAhiABDIGCAAQRRg5MgcIARAAGIAEMgwIAhAAGBQYhwIYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBwgHEAAY7wUyCggIEAAYgAQYogTSAQk1MDg0ajBqMTWoAgiwAgHxBbcQOTWZdLgu&sourceid=chrome&ie=UTF-8
#
su1,op,su2 = int(input("숫자:")),input("부호 :"),int(input("숫자:"))
result=cal(su1,op,su2)
if op == '+' or op == '-' or op == '*' or op == '/' :
    print(su1,op,su2,'=',result)
else:
    print("사칙연산만 가능합니다.") #eval()는 보안에 취약해서 if else를 통해 예외처리를함(다 안하는 조건으로)