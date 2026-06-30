#260629_day066_06_.py
class Calc_class11:
    num1 = num2 = 0
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def div(self,a,b):
        self.num1 = a
        self.num2 = b
        return self.num1 / self.num2
    def mul(self):
        return self.num1 * self.num2
    def squ(self,a,b):
        self.num1 = a
        self.num2 = b
        return self.num1 ** self.num2

obj1 = Calc_class11(0,0)

while True :
    try : 
        obj1.num1 = int(input("정수를 입력하세요:"))
        obj1.num2 = int(input("정수를 입력하세요:"))
        print("나눗셈", obj1.div(obj1.num1,obj1.num2))
        print("제곱", obj1.squ(obj1.num1,obj1.num2)) 
        break
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")
        continue
    except : 
        continue
#코딩조건에 self,x,y를 맞추기 위해 메서드 호출후 인수에 인풋으로 받은 멤버변수를 입력했습니다.
