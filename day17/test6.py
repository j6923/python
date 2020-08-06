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


    def paintEvent(self,e):
        print("페인트 이벤트 발생") #움직이거나 클릭하거나 하면 "페인트 이벤트"출력 
        qp =QPainter() #Qpaint 인스턴스 생성
         

        qp.begin(self) #페인트 이벤트 시작. #페인트 준비 시작 
        qp.setPen(QPen(Qt.red ,10)) #펜 설정, 색상은 빨간색, 크기는 10으로 한다.  
        qp.drawEllipse(QPointF(220.0,220.0),100,200) #좌표 f는 실수타입으로 된 것이고, 220.0,220.0을 가짐, 100과 200은 너비하고 높이 
        #100,200 중심점 여기 점을 가지고 F는 실수로 하려고 , 220의 220그리고 100,200 
        #타원 #좌표 f는 실수 타입으로 포인트 하나 지정, 100,200은 너비하고 높이 
        qp.setPen(QPen(Qt.blue , 10)) #펜을 지정한다, 색상은 파란색, 크기는 10으로 한다. 
        qp.drawEllipse(QPointF(0.20,0.20),100,200) #타원을 설정, 좌표로 0,20,0.20자리 너비가 100, 높이가 200자리에 그려라. 

        
        
        
        qp.setBrush(QColor(255,0,255))  #브러쉬 가운데 색상을 칠해줄 때 사용 , r, ,bu 모든 애들이 다 색깔 칠해짐. 중간에 
        qp.drawRect(30,30,100,150)


       
        qp.end() #끝을 알려줌. 중간에 그리는 것 시킴 

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())



