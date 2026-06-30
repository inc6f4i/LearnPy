class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result
#
class MoreFCal(FourCal): #이부분이 insight!! 상속하는 문법
    def div(self):
        result = self.first ** self.second
        return result
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFCal(2,4)
print(a.div())
a = FourCal(2,4)
print(a.div()) #여전히 기존 class도 동작함
print(MoreFCal(4,3).mul()) #생성자도 없는 pass임에도 불구하고
print(MoreFCal(4,3).add()) #해당클래스가 파라미터로 class를 inheritance해서
print(MoreFCal(4,3).div()) #기능을 쓸수있음
print(MoreFCal(4,3).sub()) #
print(MoreFCal(2,4).pow()) #

class SafeFCal(FourCal):
    def div(self):
        if self.second == 0:
            return "우엥웅"
        else :
            return self.first / self.second
        
c = SafeFCal(4,0)
print(c.div())

class Family:
    lastname = '김'
a1,a2 = Family(), Family()
print(a1.lastname, a2.lastname)
Family.lastname = '박'
print(a1.lastname, a2.lastname)
print('56---->',Family.lastname)

a1.lastname = "최"
print(a1.lastname, Family.lastname) #이건 당연한 얘기 아닌가? 메모리가 다른데
