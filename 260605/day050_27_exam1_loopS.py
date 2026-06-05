a = int(input("값 입력:"))
b = sorted(range(1, a+1, 2), reverse=True)
c = sorted(range(0, a+1, 2), reverse=True)
d = sorted(range(1,a+1, 1), reverse=True)
tot1 = 0; tot2 = 0; tot3 = 0;
for i in list(b):
    tot1 += i
for i in list(c):
    tot2 += i
for i in list(d):
    tot3 += i
b1 = ", ".join(map(str, list(b)))
c1 = ", ".join(map(str, list(c)))

print('-'*50)
print(f'홀수 : {b1} 홀수의합 :{tot1}')
print('-'*50)
print(f'짝수 : {c1} 짝수의합 :{tot2}')
print('-'*50)
print(f'{a}에서 1까지의 합 :{tot3}')


a1 = ['a','b','c']
