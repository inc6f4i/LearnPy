def defOdd(su):
    str = "str"
    if su%2 == 0:
        str = "짝수"
    else :
        str = "홀수"
    return str
try :
    ssu = int(input("수 입력 :"))
except :
    print("정수입력")
    exit(1) # 관례(convention) 혹은 표준 규칙, 오류로 종료되는거면 인자1로 오류보내기
print(f'입력 값 : {ssu} {defOdd(ssu)} 입니다')