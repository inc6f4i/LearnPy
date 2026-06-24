def func2(a,b):
    a +=5; b *= 10
    print(f"func2:a={a},b={b}")
    print(f"func2:a={id(a)},b={id(b)}")
def func1():
    a = 5; b = 10
    func2(a,b)
    print(f"func1:a={a},b={b}")
    print(f"func1:a={id(a)},b={id(b)}")
func1()
