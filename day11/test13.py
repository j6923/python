from test12 import parent   #test12에서 parent를 불러옴. 

class Child(parent):                       #Child클래스를 생성하고 parent를 상속받음 
    def __init__(self):                    #초기화함
        super().__init__()                 #부모의 초기화를 받음 
        self.score = 100                   #score을 100으로 함. 

    def goClub(self):                      #클럽가는 동작을 함수 goClub으로 만듦
        print("움찟~~~움찟")                #함수를 호출하면 움찟~~~움찟 출력 

    def singing(self):                     #노래부르는 동작을 singing이라는 함수로 만듦  
        print("와~~여름이다.....") #메서드 오버라이딩이라고 함. 똑같이 복사하고 고치면 됨. method overriding 다시 정의한다. 물려받은 것을 다시 정의해서 씀. 
                                   #함수가 호출되면 와~~여름이다...... 출력 
if __name__ == "__main__": #메인으로 부를 때만 쓰라고 
    c = Child()             #클래스 Child를 c에 대입해서 c라는 인스턴스를 생성 
    print(c.score)          #c의 score을 출력 
    print(c.name)           #c의 name을 출력 
    print(c.age)            #c의 age을 출력 


    c. eating()             #c의 eating을 호출 
    c.singing()             #c의 singing을 호출 
    c.goClub()              #c의 goClub을 호출 