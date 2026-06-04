#016-6
for k in [1,2]:    
    print('k', k)
    for i in [1,2,3,4,5]:
        print('i', i)
        if i == 2:
            break
        print('if문break로 탈출')
    print('for내부탈출')
print('for외부탈출')