class Car:
    def __init__(self,handle=1,wheel=4,eye=2,nose=1,mouse=1):
        self.handle = handle
        self.wheel= wheel
        self.eye = eye
        self.nose = nose
        self.mouse=mouse
        print("초기화 함수 호출..")
    def run(self):
        print(self.wheel,"붕붕카 달리는중")

    def stop(self):
        print("정지..")
    
    def smell(self, what):
        print(what,"냄새를 맡는 중")
    
    def talk(self):
        print("혼자 중얼중얼 대화중입니다.")
    
    def __add__(self,otherCar):
        print("충돌났어요 ㅠㅠ")
    #뒤에 대상을 주고 충돌났어요. 
    #상속받은 애도 있음 
    def __sub__(self, otherCar):
        print("빼요")
    

c1 = Car()

c1.talk()

c1.run()
#연산자도 오버로딩 가능 --- 파이썬 
#
print(c1.handle)
    # except expression as identifier:
    #     pass
    # else:
    #     pass
    # finally:
    #     pass


#오픈카를 만들어봅시다. --- 


class InheritedCar(Car):
    def lightOn(self):
        print("라이트를 켜요")
    
    def run(self):
        print("오픈카로 달려요")
    def smell(self, what):
        print(what,"냄새를 못 맡아요.")
    
ic1 = InheritedCar()
ic1.smell("장미")
ic1.lightOn()
ic1.run()


#연산자 오버로드가 가능
#문자일 때는 붙이는 용도
#하나의 대상이 +는 어떤 대상이냐에  오버로딩, 다중정의라고 함,
# 한번에 여러가지 의미갖음
# 객체와 객체 연산시키고 싶으면  
#add는 +전용을 위한 전용함수   

# c1 - ic2
# c1.__add__(ic1)

c1+ic1 #이렇게 해도 됨. 

c1-ic1


