# day057_08.py
ls = [10,5,20,7,9,31,12,11,19,32]
print(f'정렬전{ls}')
for i in range (10):
    for j in range (i+1, 10):
        if ls[i] > ls[j]:
            ls[i], ls[j] = ls[j], ls[i]

print(f'정렬 후{ls}')