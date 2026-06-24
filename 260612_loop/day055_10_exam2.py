for i in range (5):
    l = []
    for j in range(5):
        if i == 0:
            l = l + [i * j]
        if i == 1:
            l = l + [j]
        if i == 2:
            l = l + [i * j]
        if i == 3:
            l = l + [i * j]
        if i == 4:
            l = l + [j*4]
    print(f'상위포문{i}일때 하위 포문 :', *l)