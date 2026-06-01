# 셀 012-1
listData = ['a', 'b', 'c']
inputData1 = input('알파벳을 입력하세요:')
if inputData1 in listData: # in 연산자의 해석: listData라는 리스트의 요소 중에 'a' 라는 문자가 
                    # 존재하는 것이 True이면 '"a"가 listData에 요소로 존재합니다.'을 출력함
    print('입력문자' + inputData1 +'가 listData에 요소로 존재합니다.')
    print('참 종속문장')
else:
    print('입력문자' + inputData1 +'가 listData에 요소로 존재하지 않습니다.')
    print('거짓 종속문장')
print('거짓다음문장')
