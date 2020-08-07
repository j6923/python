import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import time 
import threading
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


    def paintEvent(self,e):   #paintEvent함수를 지정하고 e를 매게변수로 받음 
                             #e는 이벤트 대상으로 하는 객체, 
                              #e로 이벤트가 어떤 애인지 볼 수 읷음, 
                              #e를 자동으로 호출하면 뭐 때문에, 뭐 할 때, 언제 생겼는지 알 수 있음 
        print("페인트 이벤트 발생") #움직이거나 클릭하거나 하면 "페인트 이벤트"출력 ??? 뭐하는애였지?
        qp =QPainter() #Qpaint 인스턴스 생성
        qp.begin(self)  #페인트 이벤트 시작. #페인트 준비 시작

        qp.setPen(QColor(0,0,0)) #펜을 생성, 색상은 rgb의 0,0,0 
        qp.setFont(QFont("나눔고딕",50)) #폰트 크기 50 
        qp.drawText(100,100,"푸른하늘 은하수 하얀 쪽배 ")#좌측 상단 100,100위치에 글자를 써넣어 
        
        
        self.drawOther(qp)  #drawOther을 호출해 밑에 함수 
        
        qp.end() #끝을 알려줌. 중간에 그리는 것 시킴 
        #끝을 알려줌. 중간에 그리는 것 시킴 
    def drawOther(self,qp):

        pen = QPen(Qt.black,3,Qt.SolidLine) #펜은 검은색, 3으로 지정하고 solidLine은 실선 

        qp.setPen(pen)   #펜을 설정한다. 
        qp.drawLine(50,50,100,50)     #선을 그린다 x는 50, y는 50, x2는 100, y2는 50 (직선을 그림)

        pen.setStyle(Qt.DashLine) #dash는 - - - -  #큐펜을 전달해줘야 쓸 수 있어서, qp씀 
        qp.setPen(pen)         #펜을 설정한다. 
        qp.drawLine(200,50,300,150)   #선을 그린다. x는 200, y는 50, x2는 300, y2는 150 


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())


#C:\Windows\Fonts 설치된 폰트를 볼 수 있음 --다음 다음 
