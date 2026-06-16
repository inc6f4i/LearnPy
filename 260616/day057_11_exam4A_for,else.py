# 260616-실습-4-해답-ver1
# 정렬이 완성된 리스트의 각 요소에 +3 하는 소스
# 전제조건 : 소스코드 안에 이중반복문 1세트(for문이 오직 2개만 있어야 함) 만 쓸것
ls = [10,5,20,7,9,31,12,11,19,32]
i,j =0,0
print('변경전 : ',ls)
for i in range(len(ls)-1): # 여기는 변경안하고 한다면
    for j in range(i+1,len(ls)):
        if ls[i] > ls[j]:
               ls[i],ls[j] = ls[j],ls[i]
    else: 
        ls[i] = ls[i] + 3 # 기본적으로 더해주고
else: 
    ls[j] = ls[j] + 113 # 마지막꺼 더해주는거
print('변경후 : ',ls)