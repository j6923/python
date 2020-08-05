class Human:
    def __init__(self,a,b,c): #옆에 매게변수 줌 
        print("초기화 함수호출") #실행할 때 나에게 준 값으로 초기화  #값을 주면 a,b,c자리에, 그걸로 매게줘서 변경하겠다. 
        self.name = a#하면 좋음
        self.age = b
        self.job = c
        self.eye = 2
        self.mouth =1
        self.ears = 2
    def status(self):
        pass #이렇게라도 써야 실행함. 

#self는 함수명 name은 변수, 그래서 self.name이렇게 씀 
#매게변수와 변수 쓴 것 차이나면 오류 

P = Human("팽수", 20, "직장인")
P. status()

print("--------------------------------------------------")
d = Human("둘리", 100000000, "백수")
d.status()


# class car:
#     def __init__(self):
#         print("초기화함수")
#         self.company = '현대'
#         self.name = 'Sonata'
#         self.color = 'red'
#         self.year = '1년'
#         self.wheel = 1
#         self.handle = 1
#     def forward(self):
#         print("전진하자")
#     def back(self):
#         print("후진")
#     def light(self):
#         print("깜박깜박")
#     def fast(self):
#         print("가속")
#     def slow(self):
#         print("감속")
#     def stop(self):
#         print("정지")

# s = car()
# print(s.name)
# print(s.company)
# print(s.color)
# print(s.year)
# print(s.wheel)
# print(s.handle)
# s.stop()
# s.forward()
# s.back()
# s.light()
# s.fast()
# s.slow()

class car:
    def __init__(self,manu,name,color,age): #인스턴스에 주소값 생성 
        print("초기화함수 호출")
        self.manu = manu  #인스턴스 변수  #실제로 메모리 할당될 때 인스턴스 영역내에서 할당되기 때문에 이렇게 부름 
        self.name = name #변수와 의미파악 가능한 이름짓는 것이 좋음. 
        self.color = color #보통 변수의 이름만 보기 때문에 좀더 의미있게 주는 게 바람직 하다. manu, name,color, age 
        self.year = age               
        self.tire = 4
        self.handle = 1
    def forward(self):
        print("전진 합니다")
    def back(self):
        print("후진")
    def light(self):   #인스턴스 함수(메서드)라고 함 
        print("깜박깜박")
    def fast(self):
        print("가속")
    def slow(self):
        print("감속")
    def stop(self):
        print("정지")

ns = car("닛산","맥시마","silver",2019)  #이렇게 만들려고 클래스 만들고 초기화되면서 메모리에 할당 
c = car("닛산","맥시마", "silver",2019)
#특징 : 파이썬 메서드의 첫번째 파라미터명은 관례적으로 self 이름 사용 
#그래서 self 항상 들어감
# 호출시 호출한 객체 자신이 전달되기 때문 self 이름 사용 
c.forward()
ns.forward()
car.forward(c) #c라는 애 주소를 줘. 원래 자기 자신의 동작을 주소 넣어서 동작, 항상 넣어서 동작하기 때문에 ()생략, 이것을 받아주는 것이 self 
c.back()

'''
    OOP : Object Oriented Progeramming의 약자 ,, 프로그램에서 가장 중요한 객체를 놓고 그것을 중심으로 프로그램을 짜. 
   자원의 재활용이 목적(하나 잘 만들어 놓고 이것 갖다써.), 요즘 근래는 이게 추세.
   클래스를 사용해 객체(instance)를 생성
   클래스는 새로운 이름공간을 지원하는 단위

   eating() car는 forward(), back()
   할 때마다 각자 영역에 따로 이런 애들을 갖고 있게 되는것 

   isinstance(변수, 클래스명) 이 변수가 이클래스로 부터 만들어진거야? 알수 있음  
'''
print(isinstance(c,car)) #아니면 f 맞으면 true  