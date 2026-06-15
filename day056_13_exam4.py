Rice = 100*1000
rats = 2
day = 0
while Rice > 0 :
    Rice -= 20*(rats)
    day += 1
    print(day,Rice)
    while day % 10 == 0:
        rats *= 2
        print(rats)
        break
else :
    print(f'{day}일 {rats}마리')