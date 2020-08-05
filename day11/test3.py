class player:
#클래스 바로 밑에 클래스 속성 주기 가능 
    cnt = 0 #변수를 선언한 것 클래스 속성이라고 함.  
    bag = []
    def __init__(self,name):
        print("초기화 함수")    #클래스명. 변수명으로 접근함. 
        self.name = name#인스턴스 변수   #호출 내가 준 이름으로 인스턴스 출력 
        player.cnt += 1
     #하나 만들때마다 cnt는 1씩 증가 
    def put(self,obj):
        player.bag.append(obj) #사물을 담아 할 수 있음. 공용이니까 다른 애도 share가능 
    #class method
    @classmethod #bag보는 애는 class method야,self 쓸 필요없음 bag class자체에 있는 메서드이기 때문에 
    #
    def getBag(cls):
        # print("아이템",Player.cnt)
        print("아이템",cls.cnt)
    
    def attack(self,other):
        print(other.name + "를 공격합니다.") #인스턴스 함수 
    def greeting(self, other):
        print(other.name +"부모님은 잘 계시니?")

p1 = player("에코")
print(p1.cnt)
p1.put("권총")
print("-------------------------------------------------------------")
p2 = player("야스오")

print(p2.bag)
print(player.bag)
print("---------------------------------------------------------")


#클래스 속성은 : 인스턴스끼리 공유함. 인스턴스끼리 서로 공유하는 애임. 
#클래스 속성들은 cnt에 바로 생김, 저장공간 차지 
#cnt는 1로 바뀜, 인스턴스공간에 player만들고 클래스 정의된 곳 1개만 만들어짐
#p2 인스턴스 영역에는 없고 player instce에 공유함 #캐릭터끼리 물건 전달할 때 등 공용으로 쓸 때 
p1.greeting(p2) 
p1.attack(p2)
p1.getBag() #변수명 안쓰고도 이렇게 볼 수 있음 
#새로운 플래이어 는 초기화 되지 않고 남아있음 
#self는 인스턴스쪽에 가는 것, 갈 필요 없음, 인스턴스에 있는 것이 아니라 bag이라는 클래스에 있는 속서이어서 class에 가야함, class쪽에 가서 cls.bag됨 
p2.getBag()#위의 것을 이렇게 접근할 수도 있음