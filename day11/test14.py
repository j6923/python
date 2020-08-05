import random 
import math
class Agar:
    
    def __init__(self,color, nickname):
        self.radius = 5
        self.color = color 
        self.nickname = nickname 
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)
        self.weight = 10 
    
    def feeding(self,other):
        if other.weight < self.weight:
            self.weight += other.weight
        else:
            self.weight += 17 
            print("먹이주기")
        
    def split(self):
        self.weight = self.weight//2
        print("반토막나기...^^ ")
    
    def move(self):
        print("이동하기")
    def merge(self):
        self.weight += 1
        self.radius += 0.2
        print("셀 먹기 ^^")
    #2차원이어서 x, y좌표 값 가짐. 
    #@XXXXXXXXX   ---> 데코레이터 
    @staticmethod #함수 다른데서 사용할 수 있게 지정. 
    #sataticmethod는 인스턴스가 없더라도 독립적으로 사용가능. 
    def getArea(self,radius):
        return radius*radius*math.pi   #self없어도 가능
        
a1 = Agar("green", "망국이다") #초기값 줘야죠
#어떤 변수도 따로 쓰지 않았음, 따로 다른 연관이 없어, stackmethod단독적으로 쓸 수 있음, 정적인 method라고 함 , 인스턴스 하나도 없어도 실행가능 
print(Agar.getArea(50)) 
 #클래스 메서드=---클래스에 속성에 접근할 수 있는 method, 스텍틱은 완전히 독립적으로 할 수 있을 때 
 
a1.move()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.split()
print(a1.getArea(a1.radius))#에의해서 radius 주게 됨. 
    