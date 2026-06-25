# calculator3.py -> FourCal 
class FourCal :
    def __init__(self,first,second):
        self.first = first
        self.second = second
        self.result = 0

    def setdata(self, first, second) :
        #print('self.first 할당직전 first,second ',id(first), id(second))
        #print('self.first 할당직전 self.first, self.second ',id(self.first), id(self.second))
        self.first = first
        self.second = second
        #
        print('self.first 할당직후 first,second ',id(first), id(second))
        print('self.first 할당직후 self.first, self.second ',id(self.first), id(self.second))
    #
    def add(self):
        self.result = self.first + self.second
        return self.result
    #
    def sub(self) : 
        self.result = self.first - self.second
        return self.result
    def mul(self):
        self.result = self.first * self.second
        return self.result
    #
    def div(self) : 
        self.result = self.first / self.second
        return self.result
#
a = FourCal(4,2)
a.add()
b = FourCal(5,6)
print(a.first)
print(a.second)
a.setdata(4, 2)
print(a.first)  # 200페이지 중 
print(a.second) # 200페이지 중 
# 
print('add매서드 호출--->',a.add())
#
print('sub매서드 호출--->',a.sub())
#

b.setdata(3, 7)
print(b.first)  # 200페이지 하 
print(b.second) # 200페이지 하 
