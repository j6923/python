import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
class MyApps(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        label1 = QLabel("집에 가~~", self)
        font1=label1.font() #폰트를 수정 
        font1.setPointSize(50)

        label1.setFont(font1) #다시 지정해줄게요. 폰트를 지정   
        btn = QPushButton("Go Home",self) #문자열 부모클래스 #사이즈 안 주면 제일 작게 구석에 둠. 
        btn.move(200,600)
        btn.resize(500,100)

        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("집에가 앱")
        self.move(10,10)
        self.setWindowIcon(QIcon(".img/instagram.png"))
        self.resize(1200,600)
        self.show()

       #화면에 글자를 적는 객체를 'Label' (객체)라고 함.  
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApps()
    sys.exit(app.exec_())