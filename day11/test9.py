#부모클래스, base class, super class (어릴 때 슈퍼맨같이)

# 자식클래스, derived class, child 

#기반이냐 파생되었냐 
#함수는 딸려오지만 변수는 안 딸려옴. 
#부모를 가리키고 싶어요. 
#부모를 가리키는 키워드가 super  


class Animal:
    def __init__(self):
        self.eyes = 2
        self.mouth = 1
        self.ears =2
    def eating(self):
        print("당근을 먹어요")
    
    def sleeping(self):
        print("쿨쿨 자요")
class Rabbit(Animal):

    def __init__(self):
        print("토끼 초기화 함수")
        self.species = "앙골라"
        self.name = "토순이"
    
    def jump(self):
        print("깡총깡총 뛰어요")

    

class monkey(Animal):
    def __init__(self):
        super().__init__() #부모의 애니멀 클래스 , __init__ 를 호출했어, 실행했어. 
        self.tale = 1
        self.species = "긴꼬리원숭이"
        self.age = 3
        self.hand = 2 
    
    def climb(self):
        print("나무를 타요")

m = monkey()

print(m.eyes)


class Whale(Animal):
    def __init__(self):
        
        self.tail = 1
        self.speices = "범고래"

    
    
    def swimming(self):
        print("헤엄을 잘 쳐요")
    
    def breathing(self):
        print("잠깐 올라와요")



#from test7 import Person #해서 옮겨와도 됨 

# 이닛호출하지만 눈이 부모한테 있음. 

