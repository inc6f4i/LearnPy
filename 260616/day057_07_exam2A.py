#260616-실습-2-해답-ver2
ls = [4, 8, 2, 7, 6]
i, j = 0, 0
print('정렬 전', ls)
for i in range(4):
    for j in range(i+1, 5):
        if ls[i] > ls[j]:
            ls[i], ls[j] = ls[j], ls[i] #왼쪽ls[i]요소에 오른쪽ls[j]요소를 할당하고
                                        #왼쪽ls[j]요소에 할당전의 ls[i]요소를 할당
                                        # 아래c코드에 비해 파이썬은 선언과동시에 바로 스왑이 가능해 편리함
                                        #c코드
                                        #temp = ls[i]
                                        #ls[i] = ls[j]
                                        #ls[j] = temp 
print('정렬 후', ls)