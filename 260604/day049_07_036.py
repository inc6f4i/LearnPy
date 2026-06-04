#018-2
n = 1
total = 0
while True :
    total = total + n
    print(n,  total)
    if total > 100000 :
        print(n)
        print(total)
        break
    n = n+1
