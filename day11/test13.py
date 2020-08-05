from test12 import parent

class Child(parent):
    def __init__(self):
        super().__init__()
        self.score = 100

    def goClub(self):
        print("움찟~~~움찟")

    def singing(self):
        print("와~~여름이다.....") #메서드 오버라이딩이라고 함. 똑같이 복사하고 고치면 됨. method overriding 다시 정의한다. 물려받은 것을 다시 정의해서 씀. 
if __name__ == "__main__": #메인으로 부를 때만 쓰라고 
    c = Child()
    print(c.score)
    print(c.name)
    print(c.age)


    c. eating()
    c.singing()
    c.goClub()