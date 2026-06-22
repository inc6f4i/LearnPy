def add_many(*para) : 
    print('para', para)
    print(type(para))
    result = 0
    for i in para:
        result = result +i
    return result

result2 = add_many(1,2,3) # 1,2,3이 튜플로 *para에 할당되어 함수가 실행됨 가변 매개변수(Arbitrary Arguments)
print(result2)
result2 = add_many(1,2,3,4,5,6,7,8,9,10)
print(result2)
