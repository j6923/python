import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap#그림 바꿀거야 
from PyQt5.QtCore import QCoreApplication,Qt #qt추가 
#*로 갖다 써도 있지만 무겁고 느려지는 단점이 있음, 메모리에 다 딸려와서
#쓰는 애들만쓰는게 기본임
import time 

import threading
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    
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

        
        self.setWindowTitle("로그인")
        self.resize(1200, 900)
        self.move(0, 0)
        self.setWindowIcon(QIcon("../img/icon.png"))
        self.show()
    def keyPressEvent(self,e):  #키를 구해 self,는 아스키코드 나옴. 
        print(e.key())
        if e.key()==Qt.Key_Left:
            #GO LEFT 써도 됨 
            self.label1.move(self.label1.x()-10,self.label1.y())
            
            print("왼쪽으로")#나오나 보려고 씀 
             #이거 대신에 함수 불러서 하면 
            #명령만 집어넣어도 되겠죠 MOVE에 X = 얼마 넣어도 됨 
        if e.key()==Qt.Key_Left:
            self.label1.move(self.label1.x()-10,self.label1.y())
        if e.key()==Qt.Key_Right:
            self.label1.move(self.label1.x()+10,self.label1.y())
        if e.key()==Qt.Key_Up:
            self.label1.move(self.label1.x(),self.label1.y()-10)
        if e.key()==Qt.Key_Down:
            self.label1.move(self.label1.x(),self.label1.y()+10)
        if e.key()==Qt.Key_Space: #e. key의 값이 스페이스 
            print("스페이스 눌림")   

            # t = threading.Thread(target=self.moveTurtle)
            # t.start() #별도의 쓰레드로 함 
    # def moveTurtle(self):
    #     print("스페이스 눌림")
    #     for i in range(10):
    #         time.sleep(0.03)
    #         self.label1.move(self.label1.x(),self.label1.y()-10)
    #     #time.sleep(1) 번갈아 가면서 해야함. 그러면은 고급기술 필요 
    #     for i in range(10):
    #         time.sleep(0.03)
    #         self.label1.move(self.label1.x(),self.label1.y()+10)
#빨리 내려갔다 올라가서 티가 안 남. 
        #time.sleep 1초가 됨, 좀쉬렴 #여기서 하면 단점이  
            t = threading.Thread(target=self.jump)
            t.start() #별도의           
    def jump(self):
        print("스페이스 눌러")
        y=30
        for i in range(11):
            time.sleep(0.03)
            self.label1.move(self.label1.x()+10,self.label1.y()-y)
            y-=6  
        # for i in range(10):
        #     time.sleep(0.03)
        #     self.label1.move(self.label1.x()+10,self.label1.y()+10)

           
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


    #외부에서 db연결하고       