#038-1
def gP(x):
    if x == 2:
        return True
    if x <=1 or x%2 ==0:
        return False
    
    for i in range(3, int(x**(1/2))+1, 2): # 수학좀 다시 배워야
        if x%i == 0:
            return False
    else:
        return True
#038-2
intList = [x for x in range(1,101)]
ret = filter(gP, intList)
for p in ret:
    print(p,end=' ')