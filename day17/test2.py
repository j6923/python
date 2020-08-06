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


    def paintEvent(self,e):   #e는 이벤트 대상으로 하는 객체, 
                              #e로 이벤트가 어떤 애인지 볼 수 읷음, 
                              #e를 자동으로 호출하면 뭐 때문에, 뭐 할 때, 언제 생겼는지 알 수 있음 
        print("페인트 이벤트 발생") #움직이거나 클릭하거나 하면 "페인트 이벤트"출력합니다.  
        qp =QPainter()       #Qpaint 인스턴스 생성 
         

        qp.begin(self)       #페인트 이벤트 시작. #페인트 준비 시작 
        qp.setPen(QPen(Qt.blue,8)) #페이트 8픽셀로 만듬 포인트 색상, 8은 크기  #펜 설정(팬객체(파랑색, 8픽셀크기))
        qp.drawPoint(self.width()/2, self.height()/2) #너비의 절반, 높이의 절반에 정 중앙에 점을 찍습니다. 포인트를 그림. 점 찍기 
        #펜위치(화면너비의 절반, 화면높이의 절반)
       
        qp.end() #끝을 알려줌. 중간에 뭐 쓰는 것은 그리는 것 시킴   #페인트 끝 

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())    



