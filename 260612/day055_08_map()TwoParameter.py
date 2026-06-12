#041-1
def myfunc(x):
    return x**2

results = map(myfunc,[0,1,2,3])
print(list(results))

#041-2 lamda는 128page
results = map(lambda x:x**2,range(4))
print(list(results))

#041-3 호출 함수의 인자가 2개인경우 활용 예제라는데 안써보면 모르겠수
X = [1,2,3,4,5]
Y = [10,9,8,7,6]
ret = map(lambda x,y: x**2+y,X,Y)
print(list(ret))