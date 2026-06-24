# 260622--실습-1-해답
def cla():
    result=0
    su1,op,su2=int(input("숫자:")),input("부호:"),int(input("숫자:"))
    if op=='+':
        result=su1+su2
        print(su1,'+',su2,'=',result)
    elif op=='-':
        result=su1-su2
        print(su1,'-',su2,'=',result)
    elif op=='*':
        result=su1*su2
        print(su1,'*',su2,'=',result)
    elif op=='/':
        result=su1/su2
        print(su1,'/',su2,'=',result)
    else:
        print("사칙연산만 가능합니다.")
cla()