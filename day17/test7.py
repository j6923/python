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


    def paintEvent(self,e):
        print("페인트 이벤트 발생") #움직이거나 클릭하거나 하면 "페인트 이벤트"출력 
        qp =QPainter() #Qpaint 인스턴스 샹성
         
         #램덤한 위치에 램덤한 색으로 직선 그리기 100개 
        # qp.begin(self) #페인트 이벤트 시작. #페인트 준비 시작 
        # for i in range(1000):    #0-999값을 하나씩 뽑는다. #램덤한 색으로 뽑기 
        #     # time.sleep(0.01)   #0.01초씩 잠을 자라. 
        #     red = random.randint(1,255)   #빨간색은 램덤으로 1-255사이의 값으로 색깔을 뽑아냄. 
        #     green = random.randint(1,255)  #rgb의 값이 255까지 있으니까 램덤으로 1-255사이의 값을 램덤하게 뽑아냄
        #     blue = random.randint(1,255) #파란색을 rgb의 값이 255까지 있으니까 램덤으로 1-255사이의 값을 램덤하게 뽑아냄
        #     pointSize = random.randint(1,25) #1-25사이의 값을 램덤하게 뽑고 pointsize에 대입 
        #     x1 = random.randint(1,800) 램덤으로 1부터 800까지의 수를 뽑고 x1에 대입,x좌표의 값 
        #     y1 = random.randint(1,800) 램덤으로 1부터 800까지의 수를 뽑고 y1에 대입,y좌표의 값
        #     x2 = random.randint(1,800) 램덤으로 1부터 800까지의 수를 뽑고 x2에 대입,x2좌표의 값
        #     y2 = random.randint(1,800) 램덤으로 1부터 800까지의 수를 뽑고 y2에 대입,y2좌표의 값
        
        #     qp.setPen(QPen(QColor(red, green, blue) , 3))
        #     qp.drawLine(x1,y1,x2,y2)
        # qp.end() #끝을 알려줌. 중간에 그리는 것 시킴 
    def paintEvent(self,e):
            self.shape()     
            threading.Thread(target=self.shape,args=(qp,))  #매게할 변수 없음. 
            t.start()
            qp.end()
        qp =QPainter() #Qpaint 인스턴스 생성   #에러남. 
        qp.begin(self) #페인트 이벤트 시작. #페인트 준비 시작 
           
        for i in range(1000):                                   #0-999값을 하나씩 뽑는다. #램덤한 색으로 뽑기 
            time.sleep(0.01)                                    #0.01초씩 잠을 자라. 
            red = random.randint(1,255)                           #빨간색은 램덤으로 1-255사이의 값으로 색깔을 뽑아냄.
            green = random.randint(1,255)                        #초록색을 rgb의 값이 255까지 있으니까 램덤으로 1-255사이의 값을 램덤하게 뽑아냄
            blue = random.randint(1,255)                          #파란색을 rgb의 값이 255까지 있으니까 램덤으로 1-255사이의 값을 램덤하게 뽑아냄
            pointSize = random.randint(1,25)                      #1-25사이의 값을 램덤하게 뽑고 pointsize에 대입                     
            x1 = random.randint(1,800)                              #램덤으로 1부터 800까지의 수를 뽑고 x1에 대입,x좌표의 값 
            y1 = random.randint(1,800)                            #램덤으로 1부터 800까지의 수를 뽑고 y1에 대입,y좌표의 값
            x2 = random.randint(1,800)                           #램덤으로 1부터 800까지의 수를 뽑고 x2에 대입,x2좌표의 값
            y2 = random.randint(1,800)                           #램덤으로 1부터 800까지의 수를 뽑고 y2에 대입,y2좌표의 값
            qp.setPen(QPen(QColor(red, green, blue) , 3))         #펜을 설정하고 색깔은 red, green, blue이고 크기는 3으로 한다. 
            qp.drawLine(x1,y1,x2,y2)                              #직선을 그리는데 x1,y1,x2,y2로 그림 
        qp.end() #끝을 알려줌. 중간에 그리는 것 시킴 
        def shape(self):  #자주 쓰니까 함수로 
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())



