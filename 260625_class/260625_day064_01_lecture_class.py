#260625_day064_01_.py
class Calc: # 소문자여도 오류가 뜨진않으나 묵시적 관례(convention)
    def __init__(self):
        self.res = 0
    def add(self, su):
        self.res += su
        return self.res
    def sub(self, su):
        self.res -= su
        return self.res
cal1 = Calc()  #cal1은 객체명이고 Calc()호출을 통해 객체생성 
cal2 = Calc()  #cal2은 객체명이고 Calc()호출을 통해 객체생성 cal1과 다른객체임

print(cal1.add(3))
print(cal1.add(4))
print(cal1.sub(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal2.sub(7))
