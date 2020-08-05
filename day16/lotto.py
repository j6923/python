import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import random 

class lotto(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600,600,800,800) 
        self.setWindowTitle("인생은 한방!")

        #라벨을 만든다
        self.label1 = QLabel("ball",self)
        self.label2 = QLabel("ball",self)
        self.label3 = QLabel("ball",self)
        self.label4 = QLabel("ball",self)
        self.label5 = QLabel("ball",self)
        self.label6 = QLabel("ball",self)

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