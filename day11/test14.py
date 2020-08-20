import random           #램덤을 불러옴 
import math             #math를 불러옴. 
class Agar:    #Agar이라는 클래스를 만듦 
    
    def __init__(self,color, nickname):                                               #초기화하고 color와 nickname으로 매게변수 줌 
        self.radius = 5                                                               #반지름을 5로 지정  
        self.color = color                                                             #색깔은 변수 color로 지정
        self.nickname = nickname                                                       # 닉네임을 변수 nickname으로 지정 
        self.x = random.randint(1,100)                                                 #1부터 100사이의 정수에서 램덤하게 뽑아 x를 지정 (왜?)
        self.y = random.randint(1,100)                                                  #1부터 100사이의 정수에서 램덤하게 뽑아 x를 지정(왜?)
        self.weight = 10                                                                #무게를 10으로 함. 
    
    def feeding(self,other):                                                           #먹이주는 동작을 함수 feeding으로 만들고 매게변수를 other로 줌. 
        if other.weight < self.weight:                                                 #만약 대상의 weight이 자기의 weight보다 작다면
            self.weight += other.weight                                                #자기의 무게에 자기의 무게 + 대상의 무게. 
        else:                                                                          #그렇지 않다면 
            self.weight += 17                                                          #자기의 무게에 자기의 무게+17을 대입 
            print("먹이주기")                                                           #함수가 호출되면 먹이주기 출력 
        
    def split(self):                                                                    #반토막나는 동작을 split이라는 함수로 만듦
        self.weight = self.weight//2                                                     #자기의 무게에 자기의 무게/2를 대입 
        print("반토막나기...^^ ")                                                         #함수가 호출되면 반토막나기...^^를 출력 
    
    def move(self):                                                                     #이동하는 동작을 move라는 함수로 만듦
        print("이동하기")                                                                #함수가 호출되면 이동하기 출력 
    def merge(self):
        self.weight += 1
        self.radius += 0.2
        print("셀 먹기 ^^")
    #2차원이어서 x, y좌표 값 가짐. 
    #@XXXXXXXXX   ---> 데코레이터 
    @staticmethod #함수 다른데서 사용할 수 있게 지정.                       #함수를 다른 곳에서 사용할 수 있게 함. 
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
    