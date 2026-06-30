#260629_day066_11_.py
errMSG0 = '0으로 나눌수 없습니다'
errMSG1 = '정수만 입력하세요'
class Calc_class12 :
    x = y = 0
    def member_clear(self, x, y) :
        self.num1 = x 
        self.num2 = y
    def div(self):
        return self.num1 / self.num2
    def squ(self):
        return self.num1 ** self.num2
while True :
    try : 
        c1 = Calc_class12()
        c1.member_clear(int(input(errMSG1)),int(input(errMSG1)))
        print("나눗셈 :", c1.div())
        print("제곱 :",c1.squ())
        break
    except ZeroDivisionError:
        print(errMSG0)
        continue
    except ValueError:
        print(errMSG1)
        continue