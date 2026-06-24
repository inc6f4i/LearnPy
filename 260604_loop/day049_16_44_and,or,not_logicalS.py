#024-1

x = 1; y = 2
strData1 = 'hello'; strData2='python'
flag1 = x == y #0
flag2 = x < y # 1
flag3 = strData1 != strData2 # 1
flag4 = strData1 > strData2 #0

print(flag1 and flag2) # 0일단하나거짓
print(flag2 and flag3) #1 1 둘다참
print(flag3 or flag4) #1 일단하나참
print(flag1 or flag4) #0 0 둘다 거짓
print(not flag1)
print(not flag2)