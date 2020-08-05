class Person:
    '''
        인간 클래스 
    '''
    # def __init__(self):
    #     print("초기화 함수")   전 
    #     self.name="홍길동"
    #     self.age = 20
    #     self.job = "도적"



    def __init__(self):
            print(id(self))
            print("초기화 함수")
            self.name="홍길동"
            self.age = 20
            self.job = "도적"
    def eating(self, what):  #method 1개 매게변수 2개 줌 
        print(what , "을/를 맛있게 먹어요")

p1 = Person()#사람이 하나 만들어 짐  초기화함수에 변수를 선언함 name, age 등 
print("id : ", id(p1))
print(p1.name)
print(p1.age)
print(p1.job)


p1.eating("사과") #---> 사과 을/를 맛있게 먹어요, what에 전달이 되서, what에 사과를 썼고 실행 

#인간하나 더 만들어 보죠
p2 = Person()
print(p2.name) #설계도가 이렇게 되어있어서 
print("--------------------------------------------------------")
print("id(p1) :", id(p1), "id(p2) : ", id(p2))



#초기화 함수는 약속된 것 