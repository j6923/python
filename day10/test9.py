#Ghost 클래스를 생성
#Ghost
#핵미사일발사()
#마린 ---> Ghost 공격
#메딕 ----> Ghost 치료 
#Ghost ---> 마린 
#Ghost ---> 메딕
#Ghost ---> Ghost


class Marine:
    def __init__(self): 
            self.hp = 100  #체력을 100 
            self.attackpoint= 4 #공격력 4      
            print("객체 초기화")
        
    def attack(self, other):
        if other.hp > 4:
            other.hp -= self.attackpoint
        else:
            print("고마 해라.. 많이 묵었다아니가?") #이러면 체력이 '-마이너스'으로 내려가는 일 없음 
            print("체력이 %d 상태입니다" %other.hp)   
    def useSteamPack(self,other):
        print("힘이 쏫아요 뿅뿅~~")
        self.hp -= 5
        print("체력이 %d 상태입니다"%self.hp)
        
    def move(self):
        print("GoGoGo")

m = Marine()
# m2 = Marine()
# for i in range(100):
    # m1.useSteamPack() #마린 하나가 병사하나 공격 




class Medic:   
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
m = Marine() 


# for i in range(100):
#     m1.useSteamPack()  #원래는 띄어서 써야함 

me = Medic()

# me.heal(m) 

#클래스 만들어 놓으면 손쉽게 객체 만들 수 있음. 
#인스턴스 변수와 method로 구성됨
#속성은 변수, 움직임은 함수로 
#자동적으로 초기화 unit 
#self. 변수이렇게 사용해야 

class Ghost:
    def __init__(self):
        self.hp = 100 
        self.attackpoint = 100

    def siegeTank(self,other):
        print("안 보인다") 

    def fire(self,other):
        print("핵공격")
    def attack(self,other):
        print("공격")
        self.hp -= 5
        print("체력이 %d 상태입니다"%self.hp)
ta = Ghost()       
ta1 = Ghost()


# for i in range(100):
#     m1.attack(m2) #마린 하나가 병사하나 공격 

m.useSteamPack(ta)
me.heal(ta)
ta.attack(m)
ta.attack(me)
ta1.attack(ta)


class SiegeTank:
    def __init__(self):
        self.hp = 100  #체력을 100 
        self.attackpoint= 5 #공격력 4      
        print("객체 초기화")
    def SiegeMode(self):
        print("변신")
        self.hp += 10
        print("체력이 %d 상태입니다"%self.hp)
    def SiegeMode_off(self):
        print("원래대로")
        self.hp -= 10
        print("체력이 %d 상태입니다"%self.hp)
    def attack(self,other):
        print("SiegeTank 공격한다")
        self.hp -= 10
        print("체력이 %d 상태입니다"%self.hp)
s = SiegeTank()
m.useSteamPack(s)
me.heal(s)
ta.attack(m)
ta.attack(me)
ta.attack(ta1)
ta.attack(s)
s.attack(m)
s.attack(me)
