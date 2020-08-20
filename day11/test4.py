class Rabbit:                                                               #Rabbit 클래스를 생성

    def __init__(self):                                                     #초기화 함수 
        print("토끼 초기화 함수")                                            #토끼 초기화 함수 출력    
        self.eyes = 2                                                       #eyes에 2대입. 눈 2개 
        self.mouth = 1                                                      #mouth에 1대입. 입 1개 
        self.ears = 2                                                       #ears에 2대입 . 귀 2개 
        self.species = "앙골라"                                              #species에 앙골라 대입. 종류는 앙골라 
        self.name = "토순이"                                                 #name에 토순이 대입. 이름은 토순이 
    
    def jump(self):                                                          #동작 점프를 jump라는 함수로 만듦 
        print("깡총깡총 뛰어요")                                              #함수 호출되면 깡총깡총 뛰어요를 출력 

    def eating(self):                                                        #먹는 동작을 eating이라는 함수로 만듦. 
        print("당근을 먹어요")                                                #당근을 먹어요를 함수가 호출되면 출력 
    
    def sleeping(self):                                                      #자는 동작을 sleeping이라는 함수로 만듦. 
        print("쿨쿨 자요")                                                    #함수가 호출되면 쿨쿨 자요를 출력 

if __name__=="__main__":                                                     #이 페이지에서만 되게 함. 
    r = Rabbit()                                                             #이게 여기 왜 들어가지? 
    print(r.eyes)                                                            #r
    r.jump()
    r.eating()
    r.sleeping()

#test5== 원숭이
#test6 === 고래

