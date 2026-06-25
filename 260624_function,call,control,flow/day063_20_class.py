# day063_20.py
class Calc ():
    def getNum(self,su1,su2):
        self.su1 = su1
        self.su2 = su2
    def add(self):
        return self.su1+self.su2
    def sub(self):
        return self.su1-self.su2
    def div(self):
        return self.su1/self.su2
    def mul(self):
        return self.su1*self.su2
callClass = Calc()

try :
    callClass.getNum(int(input("1...")),int(input("2...")))
    print("더한값\t:\t%d\n뺀값\t:\t%d\n나눈값\t:\t%d\n곱한값\t:\t%d" %(callClass.add(),callClass.sub(),callClass.div(),callClass.mul()))
except: print("정수만입력")
