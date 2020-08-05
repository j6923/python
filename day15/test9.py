import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Calculate(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()#이거 넣어야 창 열림. 

    def initUI(self):
        self.setWindowTitle("계산기")
        self.resize(500,500)
       
        self.move(300,300)
        self.btn1 = QPushButton("7",self)
        self.btn2 = QPushButton("8",self)
        self.btn3 = QPushButton("9",self)
        self.btn4 = QPushButton("+",self)
        self.btn5 = QPushButton("4",self)
        self.btn6 = QPushButton("5",self)
        self.btn7 = QPushButton("6",self)
        self.btn9 = QPushButton("-",self)
        self.btn10 = QPushButton("1",self)
        self.btn11 = QPushButton("2",self)
        self.btn12 = QPushButton("3",self)
        self.btn13= QPushButton("0",self)
        self.btn14= QPushButton("00",self)
        self.btn15= QPushButton("*",self)
        # self.btn16 = QPushButton("/",self)
        grid = QGridLayout()

        self.setLayout(grid) #메인창에 
        # grid.addWidget()
        grid.addWidget(self.btn1,1,0) #넣으라고 그랬는데 넣을 때없음. 
        grid.addWidget(self.btn2,1,1)
        grid.addWidget(self.btn3,1,2)
        grid.addWidget(self.btn4,1,3)
        grid.addWidget(self.btn5,2,0)
        grid.addWidget(self.btn6,2,1)
        grid.addWidget(self.btn7,2,3)
        grid.addWidget(self.btn9,3,1)
        grid.addWidget(self.btn10,3,2)
        grid.addWidget(self.btn11,3,3)
        grid.addWidget(self.btn12,4,0)
        grid.addWidget(self.btn13,4,1)
        grid.addWidget(self.btn14,4,2)
        grid.addWidget(self.btn15,4,3)
        # grid.addWidget(self.btn16,4,2)

   
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculate()
    sys.exit(app.exec_())
 #몇 개의 이벤트들은 