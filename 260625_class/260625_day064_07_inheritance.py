#260625_day064_07_.py
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

class Acal(Fcal):
    def pow(self):
        res = self.su1 ** self.su2
        return res
    def div(self):
        if self.su2 == 0:
            return "0으로 나눌수 없습니다"
        else:
            return super().add()

ob = Acal(2,2)
print(ob.div())

