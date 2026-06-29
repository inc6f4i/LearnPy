# 260629-실습-2-해답-***님_ver
class Clac_class11:
    def __init__(self, x = 0, y = 0):
        print('객체 생성')
        self.num1 = x
        self.num2 = y

    def plus(self):
        p = self.num1 + self.num2
        return p

    def minus(self):
        m = self.num1 - self.num2
        return m
    
    def div(self):
        print('나눗셈 메소드 호출')
        if self.num2 == 0:
            return 0
        
        d = self.num1 / self.num2
        return d
    
    def squ(self):
        print('제곱 메소드 호출')
        s = self.num1 ** self.num2 # x^n
        return s

INFO_MSG = '정수를 입력하세요: '

in_x, in_y = input(INFO_MSG), input(INFO_MSG)
if not in_x.isdecimal() or not in_y.isdecimal():
    print('정수를 입력하세요.\n') 
    exit(-1)

cal_obj = Clac_class11() # 객체 생성(인스턴스화)
cal_obj.num1, cal_obj.num2 = int(in_x), int(in_y)

print('나눗셈 ', cal_obj.div()) # 나눗셈 연산
print('제곱 ', cal_obj.squ())   # 제곱 연산