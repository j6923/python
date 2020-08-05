# #has - a 관계 
# 1)둘 사이가 밀접한 관계 ex) 자동차 --- 엔진 
#Composition Relationship
# 2) 둘 사이가 유연한? 느슨한 관계  #두 관계가 있음.  ex 경찰 =--- 총 (총없다고 경찰 안되는 것은 아님)
#Aggregaton Relationship 





class Engine:
    def __init__(self):
        print("GDI(Gasoline Direct Injection)엔진")
    def start(self):
        print("엔진 동작하는 중")


class Car:
    def __init__(self):
        print("붕붕카..")
        self.engine = Engine() #밀접한 관계는 (초기화할 때부터 만들어야 함)들어있어야 함, but 상속의 관계는 아님

    def run(self):
        self.engine.start()  #이것을 사용하게됨 


e = Engine()
c = Car()
c.run
    
#클래스 다이어그램 --- 시스템 설계하는 사람    