#상속 
#class 뒤에 부모 클랫스명 나는 얘를 물려받은 애야 copy paste 따로 

#다시보기 에러 
class SuperMan():                                                                                 #SuperMan을 클래스로 만듦. 
    def __init__(self, name, age, job, hobby):                                                  #초기화하고 매게변수로 name,age,job,hobby를 받아줌. 
        print("초기화함수")                                                                      #초기화함수를 호출 
        self.name= name                                                                         #name에 name을 변수로 대입 
        self.age = age                                                                          #age에 age를 변수로 대입 
        self.job = job                                                                          #job에 job을 변수로 대입 
        self.hobby = hobby                                                                      #hobby에 hobby을 변수로 대입 


    def fly(self):                                                                              #나는 동작을 fly라는 함수로 만듦. 
        print("비행 : 날아보아요. ~~~")                                                          #함수가 호출되면 비행: 날아보아요.~~~를 출력 
        print("어린시절 모두 해봤잖아요 : 비행... 비행청소년...")                                  #함수가 호출되면 "어린시절 모두 해봤잖아요 : 비행... 비행청소년..."출력 

    def laser(self):                                                                            #레이저를 쏘는 동작을 laser라는 함수로 만듦.
        print("찌이잉~~~")                                                                       #함수를 출력하면 찌이잉~~~출력 


    # def eating(self, what):                                                                   #먹는 동작을 
    #     print(self.name,"이", what , "을/를 맛있게 먹어요")


    # def sleeping(self):
    #     print("쿨쿨 자요")

sm = SuperMan("슈퍼맨",20,"신문기자","연애")  #객체 지향의 핵심은 코드의 재사용. 
#프로그램 세계도 상속이라는 것이 가능 

sm.fly()
sm.laser()
sm.eating("바나나")
sm.sleeping()



    