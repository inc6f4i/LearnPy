# day058_09.py
stD = "Python study with Notion AI"
vo = 0
for i in range(len(stD)):
    if stD[i] in 'aeiouAEIOU':
        vo += 1
print(vo)
#srD[i].lower() 소문자로 비교