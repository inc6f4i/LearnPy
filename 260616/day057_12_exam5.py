ls = [10,5,20,7,9,31,12,11,19,32]
odd, even, off = [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]
a,b = 0,0
for i in range(len(ls)):
    if i%2 == 0:
            odd[a] = ls[i]
            a += 1
    else :
        even[b] = ls[i]
        b += 1
        
for j in range(5):
    off[j] = even[j] - odd[j]

print('source : ',ls)
print('odd : ',odd)
print('even : ',even)
print('e-o : ',off)