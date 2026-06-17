# day058_05.py
n = int(input("입력..."))
box = 0
while n > 0:
    edgt = n % 10  
    box = (box * 10) + edgt
    n = n // 10          
print(box)