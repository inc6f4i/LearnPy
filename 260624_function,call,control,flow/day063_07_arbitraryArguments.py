def sum_func(*par):
    result = 0
    print(f"type : {type(par)}")
    print(f"par : {par}")
    for num in par:
        result = result + num
        print(f"num : {num}")
    return result, sum(par)
Sum = 0
Sum = sum_func(10,20)
print(f"매개변수 2개의 함수 : {Sum}")
Sum = sum_func(10,20,30,40)
print(f"매개변수 4개의 함수 : {Sum} {sum(Sum)}")