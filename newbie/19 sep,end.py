print('#', end='')# end=''表示不换行 한국어로는 '끝'이라는 뜻입니다. 즉, print() 함수가 출력한 후에 줄 바꿈을 하지 않고, 다음 출력이 바로 이어서 나오도록 합니다. 따라서 위의 코드는 '#'을 출력한 후에 줄 바꿈 없이 다음 출력을 이어서 하게 됩니다.
print('#'*5)
name = "Alice"
phone = "010-1234-5678"
print('name:', name, 'phone:', phone) #변수 name과 phone의 값을 출력한다. name: Alice phone: 010-1234-5678
print(name,phone,sep=';') 
print(name,phone,sep='구분') 
      ### sep=';'는 print() 함수에서 여러 개의 값을 출력할 때, 각 값 사이에 ';'를 넣어 구분하라는 의미입니다. 따라서 위의 코드는 'name', 'phone'을 출력할 때, 두 값 사이에 ';'가 들어가게 됩니다. 결과적으로 출력은 'name;phone'이 됩니다.
      