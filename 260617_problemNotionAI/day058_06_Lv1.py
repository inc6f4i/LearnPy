# day058_06.py
n = int(input("입력..."))
box = 0
while n > 0:
    box = box + n%10
    n = n//10
print(box)