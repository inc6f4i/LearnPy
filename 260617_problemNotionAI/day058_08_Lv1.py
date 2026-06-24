# day058_08.py
tl = [10 , 22 , 1 , 546 , 7, 8, 7]
count = 7
counter = 0
for i in range(len(tl)):
    if tl[i] == count:
        counter += 1
print(counter)