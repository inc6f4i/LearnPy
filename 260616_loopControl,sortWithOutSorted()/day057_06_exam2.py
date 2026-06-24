ls = [4, 8, 2, 7, 6]

i, j = 0, 0

print('정렬 전', ls)

for i in range(4):

    for j in range(i+1, 5):

        if ls[i] > ls[j]:

            ls[i], ls[j] = ls[j], ls[i] # 이 부분의 의미는 무엇일까요?
"""
오름차순 정렬을 위해
인덱스[i]에 해당하는 숫자가 인덱스[j]에 해당하는 숫자보다 크면
인덱스[i]와 인덱스 [j]를 바꾸기 위해
각각 대치하여 대입합니다
ls[i] =ls[j];
ls[j] = ls[i];
j의 범위는 range(i+1 을 통해 같은 인덱스는 비교하지 않습니다)
"""
print('정렬 후', ls)