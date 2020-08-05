# from test9 import animal 
class Animal:
    def __init__(self,foots): 
        self.eyes = 2
        self.mouth = 1
        self.ears =2
        self.foots=foots

    # def eating(self):
    #     print("당근을 먹어요")


#부모에는 argument가 있는데 

class Rabbit(Animal):

    def __init__(self):
        super().__init__(4)#부모에 있는 매게변수로 받아줘서 4번 함.  #초기화함수 불러서 4집어넣어 하면 4됨 
        print("토끼 초기화 함수")
        
        self.mouth = 1
        self.ears = 2
        self.species = "앙골라"
        self.name = "토순이"
    
    def jump(self):
        print("깡총깡총 뛰어요")

    def eating(self):
        print("당근을 먹어요")
    
    def sleeping(self):
        print("쿨쿨 자요")
r = Rabbit() 
print(r.eyes)
print(r.foots)

class monkey(Animal):
    def __init__(self):
        super().__init__(4) #부모의 애니멀 클래스 , __init__ 를 호출했어, 실행했어. 
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
# 
# 안 쓰고 싶은 것도 있음 상속된 것---
#마음에 들지 않는 게 있으면 다시 정의 
# 
# 
# 
#  

