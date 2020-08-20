class player:                                                                          #player클래스를 만든다. 
#클래스 바로 밑에 클래스 속성 주기 가능 
    cnt = 0 #변수를 선언한 것 클래스 속성이라고 함.                                       #cnt는 빈 통  
    bag = []                                                                           #bag는 빈 리스트 
    def __init__(self,name):                                                           #초기화함. 
        print("초기화 함수")    #클래스명. 변수명으로 접근함.                             #초기화함수 출력 
        self.name = name#인스턴스 변수   #호출 내가 준 이름으로 인스턴스 출력              #속성이 name이라 변수로 함. name을 밑의 매게변수로 name으로 하게 함. 
        player.cnt += 1                                                                #이게 왜 나왔지? player의 cnt에 cnt+1을 대입 
     #하나 만들때마다 cnt는 1씩 증가 
    def put(self,obj):                                                                 #사물을 담는 동작을 put으로 만들고 obj로 매게변수를 받음. 
        player.bag.append(obj) #사물을 담아 할 수 있음. 공용이니까 다른 애도 share가능     #player을 대상으로 apppend(추가)하는데 obj를 추가해라. 
    #class method                                                                                  
    @classmethod #bag보는 애는 class method야,self 쓸 필요없음 bag class자체에 있는 메서드이기 때문에  #@가 뭐였지?  
    #
    def getBag(cls):                                                                   #getBag을 함수로 만들고 매게변수로 cls로 줌. 
        # print("아이템",Player.cnt)                                                    #문자열로 아이템과 Player의 cnt를 한다(다시보기)
        print("아이템",cls.cnt)                                                          #문자열로 아이템과 cls의 cnt를 한다(다시보기)
    
    def attack(self,other):                                                             #동작 공격을 함수로 attack을 만들고 매게변수로 other을 받아줌. 
        print(other.name + "를 공격합니다.") #인스턴스 함수                                #other의 name과 문자열로 를 공격합니다를 출력 
    def greeting(self, other):                                                           #동작인 인사를 함수로 greeting을 만들고 매게변수로 other을 받아줌. 
        print(other.name +"부모님은 잘 계시니?")                                           #other의 name과 문자열로 부모님은 잘 계시니? 출력 

p1 = player("에코")                                                                      #클래스 player과 매게변수인 name을 에코로 주고 p1에 대입해서 p1이라는 인스턴스 생성
print(p1.cnt)                                                                            ##이게뭐지?(다시보기)    p1의 cnt를 출력 
p1.put("권총")                                                                            #p1을 대상으로 권총을 담음. 매게변수를 권총으로 줌 
print("-------------------------------------------------------------")                    #"------------------------------------------"를 출력 
p2 = player("야스오")                                                                     #player의 이름을 야스오로 주고 p2에 대입해서 p2라는 인스턴스를 만듦. 

print(p2.bag)                                                                             #p2를 대상으로 bag를 한 것을 출력 bag는 어디에(다시보기)
print(player.bag)                                                                         #player에 bag한 것을 출력 
print("---------------------------------------------------------")                        #---------------------------출력 


#클래스 속성은 : 인스턴스끼리 공유함. 인스턴스끼리 서로 공유하는 애임. 
#클래스 속성들은 cnt에 바로 생김, 저장공간 차지 
#cnt는 1로 바뀜, 인스턴스공간에 player만들고 클래스 정의된 곳 1개만 만들어짐
#p2 인스턴스 영역에는 없고 player instce에 공유함 #캐릭터끼리 물건 전달할 때 등 공용으로 쓸 때 
p1.greeting(p2)                                               #p1으로 인사를 해라  (다시보기)
p1.attack(p2)                                                  #다시보기 
p1.getBag() #변수명 안쓰고도 이렇게 볼 수 있음 
#새로운 플래이어 는 초기화 되지 않고 남아있음 
#self는 인스턴스쪽에 가는 것, 갈 필요 없음, 인스턴스에 있는 것이 아니라 bag이라는 클래스에 있는 속서이어서 class에 가야함, class쪽에 가서 cls.bag됨 
p2.getBag()#위의 것을 이렇게 접근할 수도 있음