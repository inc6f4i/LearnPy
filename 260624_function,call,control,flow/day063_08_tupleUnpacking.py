def change(a,b,c):
    return a+10, b+20, c+20
a,b,c, = change(10,20,30) #튜플의 언팩킹 #호출...반환
d = change(1,2,3) #호출...반환
print(a,b,c,list(map(type,(a,b,c))))
print(d,type(d))