import sys  #sys를 불러온다. #sys는 시스템
from PyQt5.QtWidgets import *
#PyQt5의 QtWidgets에서 전체를 불러온다.
from PyQt5.QtGui import * 
#PyQt5의 QtGui에서 전체를 불러온다.
from PyQt5.QtCore import *
#pyQt5의 QtCore에서 전체를 불러온다.
import random 
#램덤을 불러온다.

class lotto(QWidget): lotto클래스를 만듦
    def __init__(self):  #초기화함
        super().__init__() #부모의 것을 상속받음
        self.initUI() UI를 만들거야

    def initUI(self):  initUI라는 함수를 만듦
        self.setGeometry(600,600,800,800) 
         #크기를 지정(x y 너비 높이)
         #x값 600 y 값 600 너비 800 높이 800으로 지정
        self.setWindowTitle("인생은 한방!")
        # 창틀을 인생은 한방이라고 적음

        #라벨을 만든다
        self.label1 = QLabel("ball",self)
        #라벨을 만들어 ball이라고 쓰고 label1에 대입
        self.label2 = QLabel("ball",self)
        #라벨을 만들어 ball이라고 쓰고 label2에 대입
        self.label3 = QLabel("ball",self)
        라벨을 만들어 ball이라고 쓰고 label3에 대입
        self.label4 = QLabel("ball",self)
        라벨을 만들어 ball이라고 쓰고 label4에 대입
        self.label5 = QLabel("ball",self)
        라벨을 만들어 ball 이라고 쓰고 label5에 대입
        self.label6 = QLabel("ball",self)
        라벨을 만들어 ball이라고 쓰고 label6에 대입

        #라벨에 기본이미지를 변경해준다
        self.label1.setPixmap(QPixmap("./img/lotto/q.jpg"))
        self.label2.setPixmap(QPixmap("./img/lotto/q.jpg"))
        self.label3.setPixmap(QPixmap("./img/lotto/q.jpg"))
        self.label4.setPixmap(QPixmap("./img/lotto/q.jpg"))
        self.label5.setPixmap(QPixmap("./img/lotto/q.jpg"))
        self.label6.setPixmap(QPixmap("./img/lotto/q.jpg"))
       
        
        self.label1.setGeometry(100,100,100,100)
        self.label2.setGeometry(200,100,100,100)
        self.label3.setGeometry(300,100,100,100)
        self.label4.setGeometry(400,100,100,100)
        self.label5.setGeometry(500,100,100,100)
        self.label6.setGeometry(600,100,100,100)
        
        
        
        
        self.btn = QPushButton("대박 번호 추첨",self)
        self.btn.resize(150,100)
        self.btn.move(320,650)
        self.btn.clicked.connect(self.getLotto)

        self.show()   
        
    def getLotto(self):
        lotto = []
        while True: 
            j = random.randint(1,45)  
            




        
if __name__=="__main__":
    app = QApplication(sys.argv)
    my = lotto()
    sys.exit(app.exec_())
