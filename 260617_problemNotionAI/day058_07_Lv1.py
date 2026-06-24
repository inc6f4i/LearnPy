# day058_07.py
tmpList = [10 , 22 , 1 , 546 , 7, 8]

for i in range(len(tmpList)-1):
    for j in range(i+1, len(tmpList)):
        if tmpList[i] > tmpList[j]:
            tmpList[i], tmpList[j] = tmpList[j], tmpList[i]
print(tmpList[-1])