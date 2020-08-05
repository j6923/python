#상속 
#class 뒤에 부모 클랫스명 나는 얘를 물려받은 애야 copy paste 따로 


class SuperMan:
    def __init__(self, name, age, job, hobby):
        print("초기화함수")
        self.name= name
        self.age = age
        self.job = job
        self.hobby = hobby 


    def fly(self):
        print("비행 : 날아보아요. ~~~")
        print("어린시절 모두 해봤잖아요 : 비행... 비행청소년...")

    def laser(self):
        print("찌이잉~~~")


    # def eating(self, what):   
    #     print(self.name,"이", what , "을/를 맛있게 먹어요")


    # def sleeping(self):
    #     print("쿨쿨 자요")

sm = SuperMan("슈퍼맨",20,"신문기자","연애")  #객체 지향의 핵심은 코드의 재사용. 
#프로그램 세계도 상속이라는 것이 가능 

sm.fly()
sm.laser()
sm.eating("바나나")
sm.sleeping()



    