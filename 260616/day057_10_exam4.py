# day057_10.py
ls = [10, 5, 20, 7, 9, 31, 12, 11, 19, 32]

print('정렬 전', ls)
print(len(ls))

for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[i] > ls[j]:

            ls[i], ls[j] = ls[j], ls[i]
    ls[i] += 3       

print('정렬 후', ls)