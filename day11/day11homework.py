#object , class , instance 란? 

#object는 객체라는 뜻으로, 사물을 나타낸다. 만들려는 그 사물을 말한다. 책에는 클래스로 만든 피조물을 뜻한다. 
# class는 설계도와 같은 역할을 하는 것이며, 틀과 같은 역할을 한다. 책에는 클래스란, 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면이라고 나타내고 있다. 
# instance는 어떤 객체를 만든 대상, 결과물이라고 할 수 있다.즉, class로 만들어진 그 결과물을 말한다. 책에는  클래스로 만든 객체를 인스턴스라고 한다. 즉, 인스턴스라는 말은 특정 객체가 어떤 클래스의 갹체인지를 
# 관계 위조로 설명할 때 사용한다. 

#2.오른쪽의 결과가 나오게 함. 
class Man:
    def __init__(self):
        self.name = "홍길동"
        self.eye = 2
        self.gender = '남'
        self.arm = 2
        self.age = 20
        self.job = "도적"
        self.character = "스틸"
    
    def steal(self):
        print("내꼬내꼬 다 내꼬얌!!! ")
    def run(self):
        print("헛둘 헛둘")
    def runrun(self):
        print("땀나게 달려요")
    def magic_move(self):
        print("동해 번쩍 서해 번쩍")
m = Man()

print(m.name) # 홍길동
print(m.eye) # 2 
print(m.gender)# 남
print(m.arm) # 2
print(m.age) # 20
print(m.job) # 도적
print(m.character)# 스틸 

m.steal() # 내꼬내꼬 다 내꼬얌!!! 
m.run() # "헛둘 헛둘"
m.runrun() # 땀나게 달려요
m.magic_move() # 동해 번쩍 서해 번쩍
# 3.	변수명명법?
# 1. 매서드 안에 넣는다. 
# 2. 매개변수로써 init 안에 넣는다. 
#3. underbar 하나를 사용해서 내부에서만 볼 수 있게 한다. 
#4. underbar 두개를 사용해서 강제적으로 밖에서 사용불가. 

# 4. 
# 	ex4.py 
# ----------------------------------------
# 	class Triangle 
# 	width , height
# 	getArea()
# ----------------------------------------	
# 	triangle =	Triangle (100,200) # 너비 100, 높이 200 
# 	print(triangle.getArea())  # 삼각형의 너비 구하기 


# with open("./day11/ex4.py",'w') as file:
# 5. 
# 	ex5.py
# ----------------------------------------
# 	class Rectangle
# 	width , height
# 	getArea()
# ----------------------------------------
# 	r = Rectangle(200,300)
# 	print(triangle.getArea())  # 사각형의 너비 구하기 
    
# 6.
# 	ex6.py
# 	Rectangle, Triangle  의 부모 클래스인 Figure 클래스를 
# 	작성하세요 
with open("./day11/ex7.py",'w') as file:
    print(file) 
# 7. 
# 	Rectangle, Triangle 은 Figure 클래스의 구현클래스로 코드를 변경합니다.#구현 클래스: 자식 클래스를 구현한다. 

# 8. 
# 	Rectangle, Triangle 의 getArea() 는 Figure 클래스 의 getArea() 를 
# 	method overriding 시켜줍니다. 

# 9.
# 	두점 사이의 거리를 계산하는 pythagoras()를 완성하세요 

# 	print(util.pytagoras(100,100, 200 ,200))
	
# 	참고 : math.sqrt(4) ==> 2 
import math
class util:
    def __init__(self):
        print("초기함수")
    @staticmethod
    def pytagoras(a,b,c,d):
        return math.sqrt(4)
    
util = util()
print(util.pytagoras(100,100, 200 ,200))
	
# 10.	아래의 명령이 수행될수 있는 Point 클래스를 작성하세요 
# class Point:
#     def __init__(self):
#         print("초기함수")
#     def 

    
# 	p = Point(100,100) # (x, y) 좌표 
# 	p.set_x(200)  # x좌표값을 200으로 변경
# 	p.set_y(300)  # y좌표값을 300으로 변경

# 	p.get_xy() # (200,300) 형태로 출력 
	
# 	p.move(500,300) # (200,300) ==> (500,300)
# 	                     # 메세지를 출력하고 x <= 500 y <=300을 담는다.
	
# 	참고 ) 모든 메세드는 인스턴스 메서드 모든 속성는 인스턴스 속성


	