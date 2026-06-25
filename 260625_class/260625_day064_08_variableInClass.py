class Character:
    name = "제미니"
    def __init__(self, name):
        # self.name -> 이 객체의 고유 속성
        # name -> 외부에서 받아온 파라미터(변수)
        self.name = name 
        
    def introduce(self):
        # self.name을 통해 객체의 속성을 언제든 꺼내 쓸 수 있음
        print(f"안녕, 내 이름은 {self.name}이야.")

ob1 = Character(1)

ob2 = Character(2)
print(ob1.name,"\n")
print(Character.name,"\n") #shadowing: editor warns before interpreter run
ob1.introduce()
ob2.introduce()