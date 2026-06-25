#260625_day064_11_.py
class Calc_class :
    # 변수 선언
    x = y = 0
    # 생성자 : 객체 생성 + [멤버변수 초기화] 
    def __init__(self, a, b):
        print('~~객체 생성~~')
        self.x = a # 10
        self.y = b # 20
    # 멤버 함수(기능)
    def plus(self): # self : 멤버(변수+함수) 참조 객체 
        p = self.x + self.y
        '''
        p : 지역변수 
        self.x, self.y : 전역변수  
        '''
        return p 
    def minus(self):
        m = self.x - self.y
        return m
# class(1) -> object(n) 생성 
obj1 = Calc_class(10, 20) # 생성자 -> 객체1  
# object.member()  
#print('plus = ', obj1.plus()) # plus =  30
#print('minus =', obj1.minus()) # minus = -10

obj3 = Calc_class(70,90)
#요구사항 obj3 객체생성 및 __init__에 보낼 인수로 70,90을 사용했습니다
print("plus\t{}\nminus\t{}".format(obj3.plus(),obj3.minus()))
#인스턴스의 메서드 호출을 뒤쪽으로 배치해서 직관적이도록 했습니다