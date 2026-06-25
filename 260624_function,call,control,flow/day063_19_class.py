# day063_19.py

class calc():
    def __init__(self) :
        self.result= 0
    def add(self,su1):
        self.result += su1
        return self.result
    
a = calc()

print(a.add(2))
print(a.add(3))

