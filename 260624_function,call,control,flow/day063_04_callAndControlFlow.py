def display(): #호출된 함수
    num =10 #num이 10으로 초기화
    print(f"1부터 10까지의합 :{sumFunc(num)}") #인수로 10을 던짐... 돌려준값을받고 출력함
def sumFunc(num):#호출된함수인데 파라미터가 10
    sum = 0 #초기화
    for i in range(num+1): # range함수 파라미터가 10,
        sum += i # 1to10까지 더함
    return sum # 더한값은 sum에 있는데, 이걸 호출한곳에 돌려줌

display() 
