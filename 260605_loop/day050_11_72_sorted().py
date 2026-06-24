#44-1
listData = [42, 1, 39, 27, 44, 8]
ret1 = sorted(listData)
ret2 = sorted(listData, reverse=True)
print(ret1)
print(ret2)
print(listData)

#44-2
tupleData = ('사과','배','오렌지','수박','참외')
ret = sorted(tupleData, reverse=True)
print(ret)
#44-3
strData = 'aBAb'
ret = sorted(strData, reverse=True)
print(ret)
ret1 = ''.join(ret)
print(ret1)