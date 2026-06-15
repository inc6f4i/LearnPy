#사용자에게 정수 하나를 입력받습니다. (예: 4 또는 -7)
#입력받은 숫자가 양수(0 포함)이면 "Positive", 음수이면 "Negative"를 출력하세요.
#🔥 제약 조건 1: if, else, elif 같은 조건문을 절대 사용하지 마세요.
#🔥 제약 조건 2: 삼항 연산자(A if 조건 else B)나 논리 연산자 편법(and, or)도 사용 금지입니다.
#🔥 제약 조건 3: 딕셔너리({True: "Positive", False: "Negative"})를 사용하는 꼼수도 금지합니다.


intData = int(input('정수 입력: '))

list = bin(intData)
list2 = ['Positive', 'Negative']
a = list[0]
index = "0-".find(a)
print(list2[index])

#print(list2[int(list[0])])