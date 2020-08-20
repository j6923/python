# from test9 import animal                                                                    #test9에서 animal을 가져옴. 
class Animal:                                                                                 #클래스 Animal 
    def __init__(self,foots):                                                                 #초기화하고 foots를 매게변수로 함. 
        self.eyes = 2                                                                         #eyes를 2에 대입해서 눈이 2개가 되게 함. 
        self.mouth = 1                                                                        #mouth를 1에 대입해서 입이 1개가 되게 함. 
        self.ears =2                                                                          #ears를 2에 대입해서 귀가 2개가 되게 함. 
        self.foots=foots                                                                      #변수 foots를 foots에 대입 

    # def eating(self):                                                                       #동작 먹는 것을 함수 eating으로 만듦.
    #     print("당근을 먹어요")                                                               #함수가 호출되면 당근을 먹어요 출력 


#부모에는 argument가 있는데 

class Rabbit(Animal):                                                                         #클래스 Rabbit을 생성하고 animal을 상속받음                                                               

    def __init__(self):
        super().__init__(4)#부모에 있는 매게변수로 받아줘서 4번 함.  #초기화함수 불러서 4집어넣어 하면 4됨       #부모의 것을 상속받음. 
        print("토끼 초기화 함수")                                                                            #문자열 토끼 초기화 함수를 출력 
        
        self.mouth = 1                                                                                      #1을 mouth에 대입해서 입이 1이 되게 함. 
        self.ears = 2                                                                                       #2을 ears에 대입해서 귀가 2가 되게 함. 
        self.species = "앙골라"                                                                              #앙골라를 species로 대입해서 종류가 앙골라가 되게 함. 
        self.name = "토순이"                                                                                 #토순이를 name에 대입해서 이름이 토순이가 되게 함. 
    
    def jump(self):                                                                                          #점프하는 동작을 함수 jump로 만듦 
        print("깡총깡총 뛰어요")                                                                              #함수가 호출되면 깡총깡총 뛰어요 출력 

    def eating(self):                                                                                        #먹는 동작을 함수 eating으로 만듦 
        print("당근을 먹어요")                                                                                #함수가 호출되면 당근을 먹어요 출력 
    
    def sleeping(self):                                                                                      #잠자는 동작을 함수 sleeping으로 만듦
        print("쿨쿨 자요")                                                                                    #함수가 호출되면 쿨쿨 자요를 출력 
r = Rabbit()                                                                                                 #클래스 Rabbit을 r에 대입해서 r이라는 인스턴스 생성 
print(r.eyes)                                                                                                #r의 눈을 출력 
print(r.foots)                                                                                               #r의 발을 출력 

class monkey(Animal):                                                                                         #클래스 monkey를 생성하고 Animal을 상속받음 
    def __init__(self):                                                                                       #초기화함. 
        super().__init__(4) #부모의 애니멀 클래스 , __init__ 를 호출했어, 실행했어.                               #부모의 클래스의 초기화를 호출 
        self.tale = 1                                                                                          #tale에 1을 대입하여 꼬리가 1이게 함. 
        self.species = "긴꼬리원숭이"                                                                           #species에 긴꼬리원숭이를 대입해서 종류가 긴꼬리원숭이가 되게 한다. 
        self.age = 3                                                                                           #age에 3을 대입해서 나이가 3이 되게 한다. 
        self.hand = 2                                                                                          #hand에 2를 대입해서 손이 2가 되게 한다. 
    
    def climb(self):                                                                                           #오르는 동작을 함수 climb으로 만듦
        print("나무를 타요")                                                                                    #함수가 호출되면 나무를 타요를 출력 

m = monkey()                                                                                                   #monkey클래스를 m에 대입해서 인스턴스 m을 만듦 

print(m.eyes)                                                                                                   #m의 눈을 출력 


class Whale(Animal):                                                                                            #클래스 Whale을 생성하고 부모 Animal을 상속받음 
    def __init__(self):                                                                                         #초기화함. 
        
        self.tail = 1                                                                                            #tail에 1을 대입해서 꼬리가 1이 되게 한다. 
        self.speices = "범고래"                                                                                   #speices에 범고래를 대입해서 종류가 범고래가 되게 한다. 

    
    
    def swimming(self):                                                                                          #헤엄치는 동작을 함수 swimming으로 만듦 
        print("헤엄을 잘 쳐요")                                                                                    #함수를 호출하면 헤엄을 잘 쳐요 출력 
    
    def breathing(self):                                                                                          #숨쉬는 동작을 breathing으로 함수를 만듦 
        print("잠깐 올라와요")                                                                                     #함수가 호출되면 잠깐 올라와요 출력 



#from test7 import Person #해서 옮겨와도 됨 

# 이닛호출하지만 눈이 부모한테 있음.
# 
# 안 쓰고 싶은 것도 있음 상속된 것---
#마음에 들지 않는 게 있으면 다시 정의 
# 
# 
# 부모에게 상속을 받았지만 마음에 안 들면 다시 넣고 정의하면 됨. 
#  

