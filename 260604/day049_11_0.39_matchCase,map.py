#020-3
point = tuple(map(int, input().replace(',',' ').split()))

match point :
    case (0,0):
        print('원점좌표')
    case (x,0):
        print(f'x축위의 점이며 x의 값은{x}')
    case (0,y):
        print(f'y축위의 점이며 y의 값은{y}')
    case (x,y):
        print(f'x,y = ({x},{y})')
    case _:
        print('2차원 좌표가 아님')

print(type(point))
print(point)