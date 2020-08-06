import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        #창 타이틀(점찍기)
        self.setWindowTitle("점찍기")      #창 타이틀에 "점찌기"로 지정합니다. 
        #크기와 위치
        self.setGeometry(100,100,800,600)  #창의 크기와 위치를 지정합니다. 
        #화면에 보이게 설정
        self.show()                        #화면에 보이게 설정합니다. 


    def paintEvent(self,e): #paintEvent e를 매게변수로 받음. 
        print("페인트 이벤트 발생") #움직이거나 클릭하거나 하면 "페인트 이벤트"출력 
        qp =QPainter() #Qpaint 인스턴스 샹성
         

        qp.begin(self) #페인트 이벤트 시작. #페인트 준비 시작 
        
        qp.setBrush(QColor(255,0,255))  #브러쉬는 색상을 가운데 채워줄 때 사용.한번 지정하면 아래의 것도 다 동일한 색깔 칠해짐.  
        qp.drawRect(30,30,100,150)  #사각형을 x를 30, y는 30, 높이는 100, 너비는 150으로 그려라 


        qp.drawRect(30,30,100,150)        #사각형을 x를 30, y를 30, 높이 100,너비 150에 회색으로 그려 
        qp.drawRect(200,200,100,100)      #사각형을 x를 200,y를 200, 높이는 100, 너비는 100로 해서 그려라
        qp.setPen(QPen(QColor(0,0,100),5))  #펜을 설정, 색상은 rgb의 0,0,100, 크기는 5
       
        qp.drawRect(200,200,100,100)     #사각형을 x는 200, y는 200, 높이 100, 너비 100으로 그려라 
        qp.setPen(QPen(QColor(0,0,100),5)) #펜을 설정, 색상은 rgb의 0,0,100으로 하되 크기는 5로 해라 
        qp.setBrush(QColor(0,60,100))     #브러쉬를 설정, 색상은 rgb의 0,60,100으로 해라. 

        qp.drawRect(350,200,100,100)    #사각형을 그리되 x는 350, y는 200, 높이는 100, 너비는 100으로 그려라 
        qp.setPen(QPen(QColor(0,0,100),5))  #펜을 설정하되 색상은 rgb의 0,0,100으로 하고 크기는 5로 해라. 
        qp.setBrush(QColor(1,1,10))    #브러쉬를 설정하되 색상은 rgb의 1,1,10으로 해라. 
       
        qp.drawRect(500,200,100,100)
        qp.setPen(QPen(QColor(0,100,0),5)) #펜을 설정하되 색상은 rgb의 0,100,0으로 하고 크기는 5로 해라. 
        qp.setBrush(QColor(50,50,10))    #브러쉬를 설정하되 색상은 rgb의 50,50,10으로 해라. 
        qp.drawRect(200,400,400,100) #사각형을 그려는데 x는 200, y는 400, 높이는 400, 너비는 100으로 해라. 
        qp.drawLine(200,100,600,100)  #라인을 그려라 x200,y100, x2는 600 y2 100


        qp.end() #끝을 알려줌. 중간에 그리는 것 시킴 

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())



