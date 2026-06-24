#33-1
b1 = bin(97)
b2 = bin(98)
print(b1)
print(b2)



#33-2
print( b1+ b2)

#33-3

binStr1='ob1011'
binStr2='0b1001'
int1 = int(binStr1, base=2)
int2 = int(binStr2, base=2)

binAnswer = bin(int1 + int2)
print(f'{binStr1}+{binStr2}={binAnswer}')