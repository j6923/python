import sys  #세번째 
from pyQt5.QtWidgets import QApplication, Qwidget,QpushBotton  #두번째 
from PyQt5.QtCore import QCoreApplication

class game(Qwidget):   #첫번째 얘 만들기 
    def __init__(self):
        super().__init__()
        self.initUI() 
    
    def initUI(self):
        label = QLabel("나") 
        dan.move(200,100)


        bt1 = QpushBotton("→") 
        btn1.resize(100,200)
        
        bt2 = QpushBotton("←")

        bt3 = QpushBotton("↑")
        
        bt4 = QpushBotton("↓")

        self show()

#갹체를 찍으면 움직이게 


if __name__=="__main__":
    app = QApplication(sys.argv)#실행하려고 
    ex = myapp()
    sys.exit(app.exec_())