# day063_16.py
def mulChek3(su):
    if su % 3 == 0:
        print(f"{su}은 3의 배수입니다")
    else :
        print(f"{su}은(는) 3의 배수가 아닙니다")
try :
    mulChek3(int(input("수 입력:")))
except :
    print("정수입력")
    exit(1)
