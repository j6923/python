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
        qp =QPainter() #Qpaint 인스턴스 샹성
         

        qp.begin(self) #페인트 이벤트 시작. #페인트 준비 시작 
        
        qp.setPen(QPen(Qt.red,10)) #펜 설정(빨간색 10)
       
        #drawLine(x, y, x2, y2)  xy번 지점에서 x2y2번 지점까지
        qp.drawLine(100,100,200,200) #선을 그린다 x는 100, y는 100, x2는 200, y2는 200 (직선을 그림)
        qp.setPen(QPen(Qt.green,10)) #pen을 설정 : 색은 초록색, 크기는 10
        qp.drawLine(200,100,100,200) #선을 그린다 x는 200, y는 100, x2는 100, y2는 200 (직선을 그림)
        qp.drawLine(200,100,100,200) #선을 그린다 x는 200, y는 100, x2는 100, y2는 200 (직선을 그림)
        qp.end() #끝을 알려줌. 중간에 그리는 것 시킴 


        #애플 --- 앱심사기준 어려움 

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())



