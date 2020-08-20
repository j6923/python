import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap#그림 바꿀거야 
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def goUp(self):
        #
        x = self.label1.x() #x값 y값 가져오고 +하면 증가함 
        y = self.label1.y()-50
        self.label1.move(x,y)  

    def goRight(self):#move method 안에 x y 값 줌 
        x = self.label1.x()+50 #x값 y값 가져오고 +하면 증가함 
        y = self.label1.y()
        self.label1.move(x,y)  #의 값에서 
        #print(self.albe11.x(),self.labe11.y()) #x좌표 y좌표 얻어옴. 

    def goLeft(self):
        x = self.label1.x()-10 #x값 y값 가져오고 +하면 증가함 
        y = self.label1.y()
        self.label1.move(x,y)  

    def goDown(self):
    #self.label1.move(self.label1.x(),self.label1.y()-10) 이렇게 쓸 수도 있ㅇ,ㅁ. 
        x = self.label1.x()
        y = self.label1.y()+50
        self.label1.move(x,y)  

    def initUI(self):
        #QPixmap 객체 
        #가져다가 넣고 쓰고 싶어요. 
        p_img = QPixmap("./img/turtle.gif")
        self.label1 = QLabel("(๑°ㅁ°๑)‼✧", self) #여기서는 이 글자 씀
        # self.label1 = QLabel(p.img) #위 그림 대신해서 
        self.label1.setPixmap(p_img)
        self.label1.move(100,250)
        font1 = self.label1.font()
    #안에 있으면지역변수 되니까 

        self.label1.move(100, 250)
        font1 = self.label1.font()
        font1.setPointSize(30)
        self.label1.setFont(font1)

        print(self.label1)

        btnUp = QPushButton("↑", self)
        btnUp.move(470, 650)
        btnUp.resize(60, 60)

        btnUp.clicked.connect(self.goUp)

        btnRight = QPushButton("→", self)
        btnRight.move(540, 700)
        btnRight.resize(60, 60)

        btnRight.clicked.connect(self.goRight)

        btnDown = QPushButton("↓", self)
        btnDown.move(470, 750)
        btnDown.resize(60, 60)

        btnDown.clicked.connect(self.goDown)

        btnLeft = QPushButton("←", self)
        btnLeft.move(400, 700)
        btnLeft.resize(60, 60)

        btnLeft.clicked.connect(self.goLeft)

        self.setWindowTitle("로그인")
        self.resize(1200, 900)
        self.move(0, 0)
        self.setWindowIcon(QIcon("../img/icon.png"))
        self.show()
    def keyPressEvent(self,e):
        print(e.key())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())