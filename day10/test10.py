# 1. 
# 객체 지향 구구단 
class GuGuDan():
    def __init__(self):
       self.dan = 1
    # def for i in range(1,10):
    #     print(self.dan,"*",i,"=",self.dan*i)

g = GuGuDan()

g.dan = 3 

# g.print()

# 3 * 1 = 3 

# .. 
# 3 * 9 = 27


#4. TV 객체를 생성할수 있는 클래스를 작성하세요 
	# 기능 : turnOn(), turnOff(), changeChannel(n) 
class TV:
    def __init__(self):
        print("초기화함수")
    def turnOn(self):
        print("turnOn")
    def turnOff(self):
        print("turnOff")
    def changeChannel(self,n):
        print("채널돌림")

t = TV()
t.turnOn()
t.turnOff()
t.changeChannel(10)

# 5. 
# 	아래와 같은 코드가 실행될수 있도록 HandPhone 클래스를 작성하세요 

# 	hp = HandPhone()
# 	hp.call("010-1234-5678")  #011-1111-2222에서  010-1234-5678번으로 전화거는중 
# 	hp.phone_number= "010-1234-5678" # 011-1111-2222 에서 전화번호를 010-1234-5678 로변경함 
# 	hp.connect_internet() # 인터넷에 연결되었습니다. 


class HandPhone:
    def __init__(self):
        print("초기함수")
        
        self.phone_number = "011-1111-2222"

       
            
    def call(self):
        print("011-1111-2222에서  010-1234-5678번으로 전화거는중")
    def connect_internet(self): 
        print("인터넷에 연결되었습니다.")
    
# hp.call, hp.phone_number,hp.connect_internet

hp = HandPhone()
# H.hp.call()

# hp = HandPhone()
hp.call() #011-1111-2222에서  010-1234-5678번으로 전화거는중 
hp.phone_number= "010-1234-5678" # 011-1111-2222 에서 전화번호를 010-1234-5678 로변경함 
hp.connect_internet() # 인터넷에 연결되었습니다. 

#load.j.s



        
