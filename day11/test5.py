
class monkey:                                                                                 #클래스 monkey를 만듦 
    def __init__(self):                                                                       #초기화함. 
        self.eyes = 1                                                                         #eyes에 1을 대입해서 눈은 1개를 만듦, 속성이라 변수로 씀 
        self.ears = 2                                                                         #ears에 2을 대입해서 귀는 2개를 만듦, 속성이라 변수로 씀. 
        self.mouth = 1                                                                        #mouth에 1을 대입해서 입은 1개를 만듦, 속성이라 변수로 씀. 
        self.tale = 1                                                                         #tale에 1을 대입해서 꼬리를 1개를 만듦, 속성이라 변수로 씀. 
        self.species = "긴꼬리원숭이"                                                          #species에 긴꼬리원숭이를 대입해서 종류는 긴꼬리원숭이로 함. 
        self.age = 3                                                                          #age에 3을 대입헤서 나이는 3살로 함. 
        self.hand = 2                                                                         #hand에 2를 대입해서 손은 2개로 함. 
    
    def climb(self):                                                                          #올라타는 동작을 climb이라는 함수로 만들음 
        print("나무를 타요")                                                                   #함수를 호출하면 나무를 타요 출력 
    
    def eating(self):                                                                         #먹는 동작을 eating이라는 함수로 만듦. 
        print("잡식성")                                                                        #함수를 호출하면 잡식성을 호출 
    
    def sleeping(self):                                                                       #잠자는 동작을 sleeping이라는 함수로 만듦. 
        print("쿨쿨 자요")                                                                     #함수를 호출하면 쿨쿨 자요 출력 


m = monkey()                                                                                  #클래스 monkey 를 m에 대입해서 인스턴스 m을 생성 

print(m.eyes)                                                                                 #m의 eyes를 출력 
print(m.ears)                                                                                 #m의 ears를 출력 
print(m.mouth)                                                                                #m의 mouth을 출력 
print(m.tale)                                                                                 #m의 tale을 출력 
print(m.species)                                                                              #m의 species을 출력 
print(m.age)                                                                                  #m의 age을 출력 
print(m.hand)                                                                                 #m의 hand을 출력 

m.climb()                                                                                     #m을 대상으로 함수 climb 호출 
m.eating()                                                                                    #m을 대상으로 함수 eating 호출 
m.sleeping()                                                                                  #m을 대상으로 함수 sleeping 호출 

