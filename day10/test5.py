# class Marine:
    # hp = 0 #속성여기써도 되고 #초기화에 써도 됨. 
#     def __init__(self):
#         self.hp = 100  #체력을 100 
#         self.attackpoint= 4 #공격력 4 
#         print("객체 초기화")
    
#     def attack(self, other):
#         other.hp -= self.attackpoint
#         print("체력이 %d 상태입니다" %other.hp)
    
#     def move(self):
#         print("GoGoGo")  전 
    
# m1 = Marine() #마린 병사하나 
# m2 = Marine()#마린 병사하나 
# m1.attack(m2) #마린 하나가 병사하나 공격

# class Marine:
#     def __init__(self):
#             self.hp = 100  #체력을 100 
#             self.attackpoint= 4 #공격력 4 
#             print("객체 초기화")
        
#     def attack(self, other):
#         if other.hp > 4:
#             other.hp -= self.attackpoint
#         else:
#             print("고마 해라.. 많이 묵었다아니가?") #이러면 체력이 '-마이너스'으로 내려가는 일 없음 
#             print("체력이 %d 상태입니다" %other.hp)   
        
#     def move(self):
#         print("GoGoGo")

# m1 = Marine()
# m2 = Marine()

# for i in range(100):
#     m1.attack(m2) #마린 하나가 병사하나 공격 




class Marine:
    def __init__(self): 
            self.hp = 100  #체력을 100 
            self.attackpoint= 4 #공격력 4 
            print("객체 초기화")
        
    def attack(self, other):
        if other.hp > 4:     #만약 다른 체력이 4보다 크면 
            other.hp -= self.attackpoint   #다른 마린의 체력은 attackpoint를 마이너스함 
        else:
            print("고마 해라.. 많이 묵었다아니가?") #이러면 체력이 '-마이너스'으로 내려가는 일 없음 
            print("체력이 %d 상태입니다" %other.hp)   #그렇지 않으면 이거 출력 
    def useSteamPack(self):
        print("힘이 쏫아요 뿅뿅~~")
        self.hp -= 5
        print("체력이 %d 상태입니다"%self.hp)
        
    def move(self):
        print("GoGoGo")

m1 = Marine()
m2 = Marine()
for i in range(100):
    m1.useSteamPack() #마린 하나가 병사하나 공격 



# class medic:
#     def __init__(self):
#         self.hp = 100  #체력을 100 
#         self.attackpoint= 4 #공격력 4 
#         print("객체 초기화")                             내가 만든것 
#         self.SteamPack = "스팀팩"
#     def heal(self):
#         print("치료해라")
#     def move(self):
#         print("이동해라")
#     def hold(self):
#         print("그 자리를 지켜라.")


# me = Medic()
# me.heal(m1) #마린의 체력 10정도 증가 

class Medic:   #초기화 
    def __init__(self):
        self.hp = 100
        self.x = 100
        self.y = 100
        self.mp = 50
        self.healPower = 7
        self.defense = 3

    def move():
        print("GoGoGo")

    def hold(self):
        print("현재 위치를 사수합니다....")
    
    def heal(self, target):
        target.hp += self.healPower #대상의 체력을 자신의 힐링포인트 만큼 증가시킴 
        print("대상의 체력은 :", target.hp, "입니다")
m1 = Marine() 
m2 = Marine()

for i in range(100):
    m1.useSteamPack()  #원래는 띄어서 써야함 

me = Medic()

me.heal(m1) 

#클래스 만들어 놓으면 손쉽게 객체 만들 수 있음. 
#인스턴스 변수와 method로 구성됨
#속성은 변수, 움직임은 함수로 
#자동적으로 초기화 unit 
#self. 변수이렇게 사용해야 



