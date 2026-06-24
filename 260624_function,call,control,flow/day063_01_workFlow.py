def showAvrg(a,b,c):
    print("{}와{}의 평균".format(a,b))
    print("값은{}입니다".format(round(c,1)))
def avrg(j,k):
    total = j + k
    ff = total /2
    return ff
i = 2; j=3
f =avrg(i,j)
showAvrg(i,j,f)
print("다음문장 실행")