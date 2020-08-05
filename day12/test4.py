#Gun 클래스 

class Gun:
    def __init__(self,name,bullet):
        self.bullet = bullet #만들면서 몇 발인지 정하기 위해 매게 변수씀
        self.name = name 

    def fire(self):
        if self.bullet >= 1:
            print("빵야~~") 
            self.bullet -=1 #총알이 한 발 줄어듬
        else:
            print("틱~")
    
    def reload(self):
        print("찰카닥")
        self.bullet = 20 
        #총이 가지고 있는 맥스값 지금 총을 맥스값으로 세팅가능
        #현재 갯수만큼만 장정하든가 가능 지금은 스무바정도만 
         
        #여기에 self.해줘야 매게변수로 받을 수 있음. 
# g = Gun("AK47", 20)
# for i in range(20):
#     g.reload()
# g.fire() #발사 

class police:     #(Gun)
    def __init__(self,name,position,age):
        # super().__init__("k2", 20)
        self.name = name
        self.position = position
        self.age = age
        self.gun = None #총이 있을 수 있고 없을 수 있음, 기본값으로 아무것도 없어요, 해줌.
    def receive_gun(self,gun): #받으면 써야함  통해서 총을 전달받을 때만 씀
        self.gun = gun  

    def patrol(self):
        print("순찰중.. ...")

    def arrest(self, who):
        print(who, "를 체포합니다.")

    def notify_mranda_rights(self):
        print("당신은 묵비권을.....")
    
    def eat_donut(self):
        print("냠냠...")

    def use_Weapon(self):
        if self.gun != None:
            self.gun.fire()
        else : 
            print("없네.. 당황...")
    
    #호출해서 매게변수 주면 초기됨. 총이 있으면 총을 사용 

# p=police("smith","순경",20)
# # print(p.name("smith"))

# p.patrol()
# p.arrest("너")
# p.notify_mranda_rights()
# p.eat_donut()
# # p.fire()

#두 대상의 관계가 A is B되어야 함, 홍길동은 사람이다. 
#토끼는 포유류이다. 매핑되면 상속의 관계 
#총이 경찰이다? 경찰이 총이다??? 상속하면 안됨. is a 
#경찰은 총을 소지한다, has a 좀 다르게 처리 

g = Gun("m60리볼버",8)

p = police("포돌이", "순경", 20)

#p.receive_gun(g) #지급받으면 print가 없어서 안됨. 


p.use_Weapon() #지급못 받으면 

#매게변수 따로 받아서 해야지 됨. 
# del #소멸자 넣고 만들어도 됨 drop은 
# 
# 

