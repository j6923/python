# 5. 
# 	ex5.py
# ----------------------------------------
# 	class Rectangle
# 	width , height
# 	getArea()
# ----------------------------------------
# r=Rectacngle(200,300)
# print(r.getArea()) # 사각형의 너비 구하기 
    
# import ex6
from ex6 import Figure
class Rectangle(Figure):
    def __init__(self,width,height):
        super().__init__(width,height)
        
        # self.width = width  
        # self.height = height

    def getArea(self):
        return self.width*self.height

r = Rectangle(200,300)
print(r.getArea())
