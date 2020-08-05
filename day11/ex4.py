# 4. 
# 	ex4.py 
# ----------------------------------------
# 	class Triangle 
# 	width , height
# 	getArea()
# ----------------------------------------	
# 	triangle =	Triangle (100,200) # 너비 100, 높이 200 밑변곱하기 윗변 나누기 2 
# 	print(triangle.getArea())  # 삼각형의 너비 구하기 

import ex6
class Triangle(ex6.Figure):
    def __init__(self,width,height):
        super().__init__(width,height)
        
    
    def getArea(self):
        return self.width*self.height/2


triangle = Triangle(100,200)
print(triangle.getArea())


