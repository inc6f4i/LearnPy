a = int(input())
tot1 = 0; tot2 = 0
for i in range(1,a+1,2):
        tot1 += i
for i in range(0,a+1,2):
    tot2 += i
print(f'덧셈타입 1에서 {a} 까지')
print(f'홀수의 합 : {tot1}')
print(f'짝수의 합 : {tot2}')

tot1 = 0; tot2 =0;
for i in range(1, a+1):
    if i % 2 == 0 :
         tot2 += i
    elif i % 2 == 1 :
         tot1 += i
print(f'나눗셈타입 1에서 {a} 까지')
print(f'홀수의 합 : {tot1}')
print(f'짝수의 합 : {tot2}')