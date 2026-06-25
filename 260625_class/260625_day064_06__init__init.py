#260625_day064_06_.py
# 프로그램의 초기 설정값 (보통 전역 변수나 설정 파일에서 가져옴)
a = 100
B = 400
glo = 1000
class Fcal():
    # 외부 변수를 기본값으로 지정할 수도 있습니다.
    def __init__(self, su1=a, su2=B):
        self.su1 = su1
        self.su2 = su2
    
    def add(self):
        return self.su1 + self.su2 + glo

# 굳이 인수를 안 던져도 시스템 기본값(100, 200)으로 자동 세팅됨
ob = Fcal()
print(ob.add()) # 출력: 300

