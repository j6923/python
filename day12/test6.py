class player():
    def __init__(self,hp,name):
        self.hp = hp
        self.name = name 
        self.Knife = None 
        self.Su = None 
        self.Bomb = None 
        self.Gun = None 
        
    def receive_Su(self):
        if self.Su != None:
            hp += 10
            print("hp가 10증가")
             
            
        else : 
            print("없어")
    
    def receive_Knife(self):
        if self.Knife != None:
            print("꺼내기")
        else : 
            print("집어넣기")

    def receive_Bomb(self):
        if self.Bomb != None:
            hp += 20
            print("체력이 20증가")
        else : 
            print("폭탄없다")

    def receive_Gun(self): 
        if self.Gun != None:
              print("총있다")
        else: 
            print("총없다")

class Su():
    def __init__(self):
        pass
    
    def throw(self):
        print("펑")


class Knife():
    def __init__(self):
        pass

    def ready(self):
        print("준비하시고 ")

    def th(self):
        print("찌르기")


class Bomb():
    def __init__(self):
        pass

    def throw(self):
        pass 


class Gun():
    def __init__(self,name, bullet):
        self.name = name
        self.bullet = bullet 

    def fire(self,bullet):
        if self.bullet >= 1:
            print("bang")
        else:
            print("틱")
    def reload(self, bullet):
        print("장전합니다.")
        self.bullet = 15


p = player(100, "smith")
k = Knife()
b = Bomb()
g = Gun("k2", 20)  
p.receive_Su()

# g = Gun("m60리볼버",8)


p.receive_Gun() 
#지급받으면 print가 없어서 안됨. 


# p.use_Weapon() #지급못 받으면 

# self.hp = hp
print(p.name)  

        # self.Knife = None 
        # self.Su = None 
        # self.Bomb = None 
        # self.Gun = none 
# #서든어택 


#player 
#hp
#name


#수류탄
#데미지 

#칼
#
#폭탄 
#총
