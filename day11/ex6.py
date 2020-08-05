# 6.
# 	ex6.py
# 	Rectangle, Triangle  의 부모 클래스인 Figure 클래스를 
# 	작성하세요 

class Figure:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getArea(self):
        return "도형"






































# class Figure:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

# class Triangle(Figure):
#     def __init__(self):
#         super().__init__(100,100)
#         print("삼각형 초기화 함수")
    
#     def getArea(self,width,height):
#         return width*height/2


# class Rectacngle(Figure) : 
#     def __init__(self,width,height):
#         super().__init__()
#         print("사각형 초기화 함수")
#     def getArea(self):
#         return self.width*self.height
    

# t = Triangle()
# print(t.width)