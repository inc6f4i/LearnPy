#260615-실습-2-해답
num, result, i = 0, 0, 1
while True:
    num = int(input("10~20사이의 숫자입력:"))
    if num < 10 or num > 20:  #입력한 숫자가 10 미만이거나 20 초과면 while 문의 처음으로 이동합니다.
        print("잘못 입력 다시")
        continue
    break
while i <= num:
    result += i; i += 1
else:
    print("1~", num, "까지의 합 : ", result)
#