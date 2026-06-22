a=1
def local(c):
   global a #전역변수 1이 담긴 a를 가져와서 작업한다는뜻
   a = a+1
local(2) #글로벌 함수는 인자를 매개변수에 던져도 의미가없음
print(a)