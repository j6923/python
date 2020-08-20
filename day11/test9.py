#부모클래스, base class, super class (어릴 때 슈퍼맨같이)

# 자식클래스, derived class, child 

#기반이냐 파생되었냐 
#함수는 딸려오지만 변수는 안 딸려옴. 
#부모를 가리키고 싶어요. 
#부모를 가리키는 키워드가 super  

                                                                                                      #부모임>>>>> Animal이 monkey나 Whale보다 큰 개념, 그러므로 Animal이 포함함. 
class Animal:                                                                                         #Animal 클래스를 만듦>>>>> 부모클래스임.                                                                           
    def __init__(self):                                                                               #초기화함. 
        self.eyes = 2                                                                                 #eyes에 2를 대입해서 eyes가 2가 되게 함. 
        self.mouth = 1                                                                                #mouth에 1을 대입해서 mouth가 1이 되게 함. 
        self.ears =2                                                                                  #ears에 2를 대입해서 ears가 2가 되게 함. 
    def eating(self):                                                                                 #먹는 동작을 함수 eating으로 만듦.
        print("당근을 먹어요")                                                                         #함수가 호출되면 당근을 먹어요를 출력 
    
    def sleeping(self):                                                                               #잠자는 동작을 sleeping으로 함수를 만듦
        print("쿨쿨 자요")                                                                             #함수를 호출하면 쿨쿨 자요를 출력 

class Rabbit(Animal):                                                                                 #Rabbit클래스를 생성하고 Animal을 상속받음                                                                                   

    def __init__(self):                                                                               #초기화함. 
        print("토끼 초기화 함수")                                                                      #토끼 초기화 함수를 출력 
        self.species = "앙골라"                                                                       #species에 앙골라를 대입하여 종류를 앙골라가 되게 한다. 
        self.name = "토순이"                                                                          #name을 토순이로 한다. 
    
    def jump(self):                                                                                   #동작 점프를 jump라는 함수로 만듦
        print("깡총깡총 뛰어요")                                                                       #함수가 호출되면 깡총깡총 뛰어요를 출력  

    

class monkey(Animal):                                                                                 #클래스 monkey를 생성하고 Animal을 상속받음 
    def __init__(self):                                                                               #초기화함수 
        super().__init__() #부모의 애니멀 클래스 , __init__ 를 호출했어, 실행했어.                        
        self.tale = 1                                                                                 #꼬리를 1개함. 
        self.species = "긴꼬리원숭이"                                                                  #종류를 긴꼬리원숭이로 함. 
        self.age = 3                                                                                  #나이를 3으로 함. 
        self.hand = 2                                                                                 #손을 2개로 함. 
    
    def climb(self):                                                                                  #오르는 동작을 함수 climb으로 함. 
        print("나무를 타요")                                                                           #함수를 호출하면 나무를 타요 출력 

m = monkey()                                                                                          #monkey클래스를 m에 대입하여 인스턴스를 생성 

print(m.eyes)                                                                                         #m의 eyes를 출력 


class Whale(Animal):                                                                                  #Whale이라는 클래스를 생성해서 Animal을 상속받음 
    def __init__(self):                                                                               #초기화함. 
        
        self.tail = 1                                                                                 #꼬리를 1개로 함. 
        self.speices = "범고래"                                                                       #종류를 범고래로 함. 

    
    
    def swimming(self):                                                                               #헤엄치는 동작을 함수 swimming으로 만듦. 
        print("헤엄을 잘 쳐요")                                                                        #함수가 호출되면 헤엄을 잘 쳐요를 출력 
    
    def breathing(self):                                                                              #숨쉬는 것을 bereathing으로 함수를 만듦
        print("잠깐 올라와요")                                                                         #함수를 호출하면 잠깐 올라와요로 출력 



#from test7 import Person #해서 옮겨와도 됨 

# 이닛호출하지만 눈이 부모한테 있음. 

