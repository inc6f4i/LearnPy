num = 10; sum = 0
def display():
    sumFunc()
    print(f"10까지의합{sum}")
def sumFunc():
    global sum #Global Scope 전역함수
    for i in range(num+1):
        sum += i
display()

# 리턴문이 하나도 없는 함수구조
