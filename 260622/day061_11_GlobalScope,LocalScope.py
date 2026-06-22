a = 1 # Global Scope
print('전역변수',id(a))
def mem(a):
    a = a + 1 # Local Scope
    print(a)
    print('내부함수',id(a))
mem(a)
print(a)