#260625_day064_05_.py
#초기화가 있을때와 없을때의 비교하기

class Fcal():
    def __init__(self, su1=0, su2=0):
        self.su1 = su1
        self.su2 = su2
    def std(self, su1, su2):
        self.su1 = su1
        self.su2 = su2
    def add(self):
        res = self.su1 + self.su2
        return res
    def sub(self):
        res = self.su1 - self.su2
        return res
    def div(self):
        res = self.su1 / self.su2
        return res
    def mul(self):
        res = self.su1 * self.su2
        return res

ob = Fcal()
print(ob.add())