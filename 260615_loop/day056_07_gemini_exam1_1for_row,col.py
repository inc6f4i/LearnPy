# $5 \times 5$ 행렬이므로 총 25번 반복하는 '단 하나의' for문만 사용합니다.
for i in range(25):
    # i를 5로 나눈 몫은 '행(줄)', 나머지는 '열(칸)'이 됩니다.
    row = i // 5
    col = i % 5
    print(row,col,' ',end='')
    if col == 4:
        print()