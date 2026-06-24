ls = [4, 8, 2, 7, 6]
i, j = 0, 0
print('정렬 전', ls)
for i in range(4):
    for j in range(i+1, 5):
        if ls[i] > ls[j]:
            ls[i], ls[j] = ls[j], ls[i] 
print('정렬 후', ls)