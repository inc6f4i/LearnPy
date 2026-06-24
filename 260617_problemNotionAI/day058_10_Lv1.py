# day058_10.py
n = int(input('입력...'))
base = 1
while n > 0 :
    base *= n
    n -= 1
print(base)