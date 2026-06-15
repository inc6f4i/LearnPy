"""
X O X O X
O X O X O
X O X O X
O X O X O
X O X O X
for문은 단 하나만 사용하기
if 문 안에서 문자열을 곱하지 않기, 오직 한번에 한글자를 출력해야합니다
"""
def xo(n) :
    if  n%2 == 0:
        print('X ',end='')
    else :
        print('O ',end='')
for i in range(0,5,1):
    x = [i, i+1, i+2, i+3, i+4]
    list(map(xo, x))
    print()

"""
print(0%2) 
print(1%2)
print(2%2)
print(3%2)
print(4%2)
"""