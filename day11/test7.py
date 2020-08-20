class Person:                                                                          #Person클래스를 생성 
    '''
        인간 클래스  #독큐먼트 스트링 #설명나올때 이거 뭐야 나오는 것 
    '''
    

    def __init__(self):                                                               #초기화함. 
            print(id(self))                                                           #self의 id(주소)를 출력(다시보기)
            print("person 초기화 함수")                                                #Person 초기화 함수를 출력 
            self.name="홍길동"                                                         #name을 홍길동으로 함. 
            self.age = 20                                                             #age는 20으로 함.
            self.job = "도적"                                                         #직업(job)을 도적으로 함.              
            #@클래스 속성갖다쓰는 클래스 속성  
    def eating(self, what):  #method 1개 매게변수 2개 줌                               #먹는 동작을 eating으로 하고 what을 매게변수로 줌. 
        print(what , "을/를 맛있게 먹어요")                                            #what의 값과 문자열로 을/를 맛있게 먹어요를 출력 

    def sleeping(self):                                                               #잠자는 동작을 sleeping이라는 함수로 만들음
        print("쿨쿨 자요")                                                             #함수가 호출되면 쿨쿨 자요라는 문구 출력 

#Person 클래스를 상속받은 superman 클래스 #변수와 함수 다 상속받음. 부모의 sleeping과 eating까지 할 수 있음. 안 써도  
class SuperMan(Person):                                                              #SuperMan클래스를 만들고 부모인 Person을 상속받게 한다. #이렇게 하면 함수만 오류 안남, 속성일 경우 오류 
    def __init__(self, name, age, job, hobby):                                       #초기화함수를 하고 name,age,job,hobby를 매게변수로 줌. 
        print("SuperMan초기화함수")                                                   #SuperMan초기화함수 출력 
        self.name= name                                                              #SuperMan의 이름인 name을 name으로 줌. 
        self.age = age                                                               #age를 변수 age로 줌. 
        self.job = job                                                               #job을 변수 job으로 줌 
        self.hobby = hobby                                                           #hobby를 변수 hobby로 줌 


    def fly(self):                                                                   #나는 동작을 함수 fly로 만듦. 
        print("비행 : 날아보아요. ~~~")                                                #함수가 호출되면 문자열로 비행 : 날아보아요. ~~~~를 출력 
        print("어린시절 모두 해봤잖아요 : 비행... 비행청소년...")                        #함수가 호출되면  어린시절 모두 해봤잖아요 : 비행... 비행청소년...출력 

    def laser(self):                                                                  #레이저 쏘는 것을 laser 함수를 만들었음 
        print("찌이잉~~~")                                                             #함수가 호출되면 찌이잉~~~을 출력 


    
sm = SuperMan("슈퍼맨",20,"신문기자","연애")  #객체 지향의 핵심은 코드의 재사용.           #SuperMan을 상속하고 name에 슈퍼맨 age에 20, job에 신문기자, hobby에 연애를 매게변수로 넣음  
#프로그램 세계도 상속이라는 것이 가능 

sm.fly()                                                                               #sm을 대상으로 fly 함수를 호출 
sm.laser()                                                                             #sm을 대상으로 laser 함수를 호출 
sm.eating("바나나")                                                                     #sm을 대상으로 eating을 넣어주고 매게변수로 바나나를 넣어줌 
sm.sleeping()                                                                           #sm을 대상으로 sleeping 함수를 호출 



    