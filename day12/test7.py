


# player has a Gun 
class Grenade:
    pass 


class Sword:
    def __init__(self,name):
        self.name = name 
    def swing(self):
        print(self.name, "을 휘둘릅니다.") 
    def use(self): #오버라이딩함, 내 방식대로 바꿔씀. 
        self.swing() #swing 휘들러요. 그냥 불러옴. 

    

class Gun(Weapon):
    def __init__(self):
        pass 
    def fire(self):
        if self.bullet >= 1:
            print("빵야~~") 
            self.bullet -=1 #총알이 한 발 줄어듬
        else:
            print("틱~")
    def fire(self):
        

    def reload(self):
        print("찰카닥")
        self.bullet = 20 
        #총이 가지고 있는 맥스값 지금 총을 맥스값으로 세팅가능
        #현재 갯수만큼만 장정하든가 가능 지금은 스무바정도만   #
         
class Weapon:
    def __init__(self):
        pass 
    def use(self): #이 무기를 사용할 거야 
        pass 
    def reuse(self):
        pass 

    #공통의 이름 지정하면 됨. #상속받는 애들로 함.  

class Player:
    def __init__(self, name):
        self.hp = 100
        self.name = name 
        self.gun = None
        self.sword = None 
    def receive_gun(self,gun): #받으면 써야함  통해서 총을 전달받을 때만 씀
        self.gun = gun  

    def use(self):
        if self. gun != None:
            self.gun.fire()
        elif self.sword != None:
            self.sword.swing()
    def receive_sword(self, weapon):
        self.weapon =weapon 

    def use(self):
        self.weapon.use() #다영성,플리모피즈라고 함. 코드 재사용성이 커짐.   


p= Player("홍길동")
s =Sword("엑스칼리버")
g = Gun()
p. receive_sword(s)
p.use() 

#클릭 하나로 하면 중구난방 -- 통합시킬 필요 있음 

