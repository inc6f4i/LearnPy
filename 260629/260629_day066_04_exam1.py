class calc_class :
    x = y = 0
    def __init__(self, a, b):
        print('~~객체 생성~~')
        self.x = a # 10
        self.y = b # 20
    #def insert(self, a, b):
    #    self.x = a
    #    self.y = b
    def plus(self):
        p = self.x + self.y
        return p
    def minus(self):
        m = self.x - self.y
        return m

obj1 = calc_class(10, 20)

print('plus = ', obj1.plus())
print('minus =', obj1.minus())
#
obj03 = calc_class(70,90)
print('plus = ', obj03.plus())
print('minus =', obj03.minus())

#코딩조건(가)
obj02 = calc_class(0,0) #코딩조건(가)

obj02.x = 200  #코딩조건(나)
obj02.y = 50

print(obj02.plus())#코딩조건(다)
print(obj02.minus())
