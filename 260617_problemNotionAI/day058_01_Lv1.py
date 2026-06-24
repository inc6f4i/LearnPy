# day058_01.py
n = int(input('입력...'))
sumbox = 0
for i in range(1,n+1):
    sumbox += i
print(f'1부터{n}까지의 합{sumbox}')