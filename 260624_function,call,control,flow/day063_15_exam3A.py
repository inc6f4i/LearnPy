# 260624-실습-3-해답-ver1
def evenOdd(num):
    if num %2 == 0:  # 2로 나눈 나머지가 0인지 판단하는 조건식
        return 0          # 조건식이 참(True) 이면 0 을 리턴함.(짝수의 의미)
    else: 
        return 1      # 조건식이 거짓(False) 이면 1 을 리턴함.(홀수의 의미)
   
num = int(input("수 입력 : "))
result = evenOdd(num)
if result == 0:
    print("입력 값 : ",num," 짝수 입니다")
else:
    print("입력 값 : ",num," 홀수 입니다")
#
#
# 260624-실습-3-해답-ver2
def evenOdd2(num):
    return '짝수' if num % 2 == 0 else '홀수'
print("입력 값 :",evenOdd2(int(input("수 입력 : "))),"입니다"  )
#3년차부턴 축약식으로 코딩
#띄어쓰기 잘하기
#언어 뉘앙스 차이? result == 0 : 이렇게 띄어쓰기
#효율적인 코딩을 위해서는? 솓고는?
#요즘은 위나 아래나 차이없고
#오히려 작성후 나중에 편집할때
#누구나 읽기 쉽고 소통이 가능해야함