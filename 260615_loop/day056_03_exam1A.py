#----------------------------------------------------------
#260615-실습-1-해답-v1
star="*"
for i in range(0,2):
    for k in range(1,4):
        if i==0:
            print("{}".format(star*(i+k)))
        else:
            print(f"{'*'*(4 - k)}")
            #print(f"{star * (4 - k)}")
print()
print()


#260615-실습-1-해답-v2
for y in range(1,7):
    for x in range(1,4):
        if y>=x and (y-x)<4:
            print("*",end="")


    print()    ### print문의 탭 위치에 주목하세요
print()   ### print문의 탭 위치에 주목하세요
print()   ### print문의 탭 위치에 주목하세요

#260615-실습-1-해답-v3
#이 버전은 별의 갯수를 range함수와  if조건식으로 제어해야 한다는
#코딩조건에 위반하지만 이런 것도 가능한 풀이방법이라는 면에서 공유합니다.
for i in [1,2,3,3,2,1]:
    for k in [1]:
        g=i*k
        print("*"*g)