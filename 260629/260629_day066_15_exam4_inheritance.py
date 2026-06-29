#260629_day066_15_.py
class Employee:
    name = None
    pay = 0
    def __init__(self, name):
        self.name = name
    def pay_calc(self):
        pass
class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)
    def pay_calc(self, base, bonus):
        self.pay = base + bonus
        print(f'총수령액 {self.pay}원')
class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)
    def pay_calc(self,tpay, time):
        self.pay = tpay*time
        print(f'총수령액 {self.pay}원')

p = Permanent('이순신')
p.pay_calc(3000000,200000)

t = Temporary("홍길동")
t.pay_calc(15000, 80)
        
class Alba(Temporary):
    def pay_calc(self, tpay, time, day):
        if time/day == 8:
            self.pay = tpay*(time+8)
            print(f'총수령액 {self.pay}원')
            #print("맞다")
        else :
            self.pay = tpay*time
            print(f'총수령액 {self.pay}원')
            return print("만근아님")

    
alba = Alba(None)
alba.pay_calc(20000, 160, 20)