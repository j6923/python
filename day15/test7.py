from threading import Thread

class MThread(Thread): #상속받은 애 MThread도  thread의 기능을 갖음 
    def __init__(self, who):
        super().__init__()
        self.who = who 

#run 함수를 override함. 
    def run(self):
        for i in range(1,100):
            print(str(i)+"미터 달리는 중", self.who)

h1 = MThread("천둥이")
h2 = MThread("각설탕")

h1.start()
h2.start()

#thread클래스를 상속받고 ,  동시에 처리할 코드를 함수에 넣고 start로 호출함. 
#파이썬은 1부분 더 선호 
#

print("찍짝짝 축하합니다... Main Thread end")

