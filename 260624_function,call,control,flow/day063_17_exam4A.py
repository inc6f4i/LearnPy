# 260624-실습-4-해답-ver1
def test(su):
    if not su % 3:    # 매개변수 su를 3으로 나눈 나머지에 
                    # not 연산을 한 조건식
        return "3의 배수 입니다" # 3으로 나눈 나머지가 0 이라면(3의배수인 경우) 
                                 # not 연산으로 참인경우 조건식 수행함 
    else:
        return "3의 배수가 아닙니다" # 3으로 나눈 나머지가 0 이 아니라면(3의배수인 경우)
                                   # not 연산으로 거짓인경우 조건식 수행함 
num = int(input("수 입력 : "))
s = test(num)
print(s)
#
#
# 260624-실습-4-해답-ver2
def test1(num) :
    return '3의 배수입니다' if num % 3 == 0 else '3의 배수가 아닙니다'
print(test1(int(input('수 입력 : ')) ))


"""
교수님은 가독성이 ver1이 좋다고 생각하심
직관적인이유


ver2는 굳이 3년차에 알아서 된다고

"""