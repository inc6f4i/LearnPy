for i in range ( 0 , 3 , 1):
    for k in range ( 0 , 5 , 1):
        if k == 3:
            break
        print("(i : %d\tk : %d)" % (i , k ))
print()
print()

i = 0; k = 0
while i <= 2:
    while k <= 2:
        print(f'(i : {i}\tk : {k})')
        k += 1
    else :
        i += 1; k = 0
