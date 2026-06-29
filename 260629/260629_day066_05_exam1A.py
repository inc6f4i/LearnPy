# 260629-실습-1-해답
# 클래스 정의
class Calc_class :
    # 변수 선언
    x = y = 0
    # 생성자 : 객체 생성 + [멤버변수 초기화]
    def __init__(self, a, b): ############생성자 이니트,특별한 이름을가진 메서드
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
#
print('plus = ', obj1.plus()) # plus =  30
print('minus =', obj1.minus()) # minus = -10
#
obj03 = Calc_class(70,90)
print('plus = ', obj03.plus())
print('minus =', obj03.minus())
#
obj2 = Calc_class(0,0)  # 객체(object)를 만들고 객체의 주소를 obj2에 할당함
                        # 이 때 인수로 0,0 을 할당함
###########################################################                        
obj2.x = 200            # 객체의 맴버변수 x에 200을 할당함 
obj2.y = 50             # 객체의 맴버변수 y에 50을 할당함
###########################################################
#멤버 변수는 객체 dot 변수명으로 제어함
print('plus = ', obj2.plus())
print('minus =', obj2.minus())

##이전까지는 객체이름.메서드이름으로 호출했으나
##이제부터는 객체이름.변수이름으로 멤버변수를 호출함