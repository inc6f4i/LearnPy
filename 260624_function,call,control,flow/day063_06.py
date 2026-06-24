def sum_func(x1,x2,x3=100):
    result = 0
    result = x1 + x2 + x3
    return result
def display():
    Sum = 0
    a,b,c = 10, 20, 30
    Sum = sum_func(a,b)
    print(f"매개변수 2개함수 호출{Sum}")
    Sum = sum_func(a,b,c)
    print(f"메게변수 3개 함수호출{Sum}")
display()

"""
원칙은 인수는 파라미터 갯수에 맞게 전달함
경우에따라 예외적으로 마지막 파라미터에 초기화를 설정함
"""