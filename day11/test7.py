class Person:
    '''
        인간 클래스  #독큐먼트 스트링 #설명나올때 이거 뭐야 나오는 것 
    '''
    

    def __init__(self):
            print(id(self))
            print("person 초기화 함수")
            self.name="홍길동"
            self.age = 20
            self.job = "도적"
            #@클래스 속성갖다쓰는 클래스 속성  
    def eating(self, what):  #method 1개 매게변수 2개 줌 
        print(what , "을/를 맛있게 먹어요")

    def sleeping(self):
        print("쿨쿨 자요")

#Person 클래스를 상속받은 superman 클래스 #변수와 함수 다 상속받음. 부모의 sleeping과 eating까지 할 수 있음. 안 써도  
class SuperMan(Person):
    def __init__(self, name, age, job, hobby):
        print("SuperMan초기화함수")
        self.name= name
        self.age = age
        self.job = job
        self.hobby = hobby 


    def fly(self):
        print("비행 : 날아보아요. ~~~")
        print("어린시절 모두 해봤잖아요 : 비행... 비행청소년...")

    def laser(self):
        print("찌이잉~~~")


    
sm = SuperMan("슈퍼맨",20,"신문기자","연애")  #객체 지향의 핵심은 코드의 재사용. 
#프로그램 세계도 상속이라는 것이 가능 

sm.fly()
sm.laser()
sm.eating("바나나")
sm.sleeping()



    