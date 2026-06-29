# 260629-실습-2-해답-ver2
class Calc_class11 :
    # 멤버변수 없음
    def __init__(self, x, y) :
        self.num1 = x  #멤버변수 self.num1를 동적으로 생성함
        self.num2 = y
    def div(self, x, y):
        return self.num1 / self.num2
    def squ(self, x, y):
        return self.num1 ** self.num2
c1 = Calc_class11(int(input("정수를 입력하세요 : ")),int(input("정수를 입력하세요 : ")))
print("나눗셈 :", c1.div(c1.num1,c1.num2))
print("제곱 :",c1.squ(c1.num1,c1.num2))
#--------------------------------------------------------------
# 260629-실습-2-해답-ver2
class Calc_class11:
    #num1 = num2 = 0
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y
    def div(self):
        return self.num1 / self.num2
    def squ(self):
        return self.num1 ** self.num2
obj = Calc_class11(int(input("정수를 입력하세요:")),int(input("정수를 입력하세요:")))
print ("나눗셈",obj.div())
print ("제곱",obj.squ())