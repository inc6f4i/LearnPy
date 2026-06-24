#53-1
fruits=('사과','배','참외','수박','배','오렌지')
pos = fruits.index('배')
print(f'배는 {pos+1}번째 과일입니다')
#53-2
pos = fruits.index('배',3) #인덱스가 3이상인 해당요소 찾기
print(f'배는 {pos+1}번째 과일입니다')