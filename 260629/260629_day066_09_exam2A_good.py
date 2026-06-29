# 260629-실습-2-해답-***님ver
class Calc_class11:

    def __init__(self,x,y):
        self.num1 = x
        self.num2 = y

    def div (self):
        d = self.num1 / self.num2
        return d
    
    def squ (self):
        s = self.num1 ** self.num2
        return s

cal1 = Calc_class11(0,0)
key = 0
while key < 2:
    calc_input = int(input(f'{key+1} 번째 정수를 입력하세요: '))
    if key == 0:
        cal1.num1 = calc_input
        #print(cal1.num1)
    elif key == 1:
        cal1.num2 = calc_input
        #print(cal1.num2)
    key += 1

print("나눗셈 : " ,cal1.div())
print("제곱 : " ,cal1.squ())