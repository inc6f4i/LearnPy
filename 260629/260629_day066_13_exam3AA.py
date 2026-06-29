# 260629-실습-3-해답_ver2
class calc_class12:
    num1 = num2 = 0
    def __init__(self,x,y):
        self.num1 = x
        self.num2 = y
    def div(self):
        return self.num1 / self.num2
    def squ(self):
        return self.num1 ** self.num2

c1 = calc_class12(int(input("정수를 입력하세요:")),int(input("정수를 입력하세요:")))
print ("나눗셈 : ",c1.div())
print ("제곱 : ",c1.squ())