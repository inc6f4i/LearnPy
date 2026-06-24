ls = [10, 5, 20, 7, 9, 31, 12, 11, 19, 32]
i, j = 0, 0


odd, even, off = [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]

for i in range(len(ls) - 1):
    for j in range(i + 1, len(ls)):      
        if i % 2 == 0:
            odd[i // 2] = ls[i]
#            print('i%2일때 i//2=',i//2)
        else:
#            pass
            even[i // 2] = ls[i]
#            print('안쪽else even i//2=',i//2)
    else: 
#        pass
        off[i // 2] = even[i // 2] - odd[i // 2]
#        print('중간 else',i//2,)
else: 
#    pass 
#    even[j // 2] = ls[j]
    off[j // 2] = even[j // 2] - odd[j // 2] 
#    print('외측 else 마지막 인덱스',j,j//2)



print('source : ', ls)
print('odd :   ', odd)
print('even :  ', even)
print('e-o :   ', off)