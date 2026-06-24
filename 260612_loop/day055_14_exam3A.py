#260612-실습-3-해답 ver-1
# 
for i in range(1,6,1): # 출력하는 줄의 수만큼 반복을 설계함
    for k in range(1,6,1): # 한 줄에 출력되는 숫자의 갯수로 설계함
         print(k+5*(i-1),end="\t") # 숫자간 띄어쓰기위해 end="\t"사용함
    print()
print()
print()
#
#------------------------------------------
#260612-실습-3-해답 ver-2
#
num = 1
su = 1
for i in range(1, 6, 1):
    num = i * 5
    for k in range(su, num+1, 1):
        print(k, end="\t")
    print()     # 줄바꿈 용도로 사용됨
    su = num + 1
print()
print()
#
#------------------------------------------------------------------
#260612-실습-3-해답 ver-3
#
for i in range(0,25,5): 
    for j in range(1,6): 
        print(i+j, end="\t") 
    print('')

