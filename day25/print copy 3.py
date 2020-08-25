import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class paint(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100,100,1000,900)
        self.setWindowTitle("누가누가 밥사나~~ 진사람이 사지!")
        frmbox = QVBoxLayout()
        self.setLayout(frmbox)
        leftbox = QVBoxLayout()
        rightbox = QHBoxLayout()
        #그룹박스 1 
        gb = QGroupBox("음식의 종류")
        leftbox.addWidget(gb)
        box1 = QVBoxLayout()
        frmbox.addLayout(leftbox)
        box1.addLayout(rightbox)
        gb.setLayout(box1)
        box1.addWidget(QRadioButton("한식",self))
        box1.addWidget(QRadioButton("중식",self))
        box1.addWidget(QRadioButton("일식",self))
        box1.addWidget(QRadioButton("양식",self))
        box1.addWidget(QRadioButton("디저트",self))
        
        #그룹박스 2 
        gb1 = QGroupBox("메뉴")
        leftbox.addWidget(gb1)
        frmbox.addLayout(leftbox)
        frmbox.addLayout(rightbox)
        box2 = QVBoxLayout()
        gb1.setLayout(box2)
        gb1.setLayout(box2)
        box2.addWidget(QCheckBox("닭볶음탕",self))
        box2.addWidget(QCheckBox("곰탕",self))
        box2.addWidget(QCheckBox("설렁탕",self))
        box2.addWidget(QCheckBox("카페",self))
        box2.addWidget(QCheckBox("디저트",self))
        box2.addWidget(QCheckBox("백숙",self))
        
        
        self.view = CGView(self) 
        rightbox.addWidget(self.view) 
        

        self.view = CGView1(self) 
        rightbox.addWidget(self.view) 
        self.show()

        


        gb2 = QGroupBox("지도")
        leftbox.addWidget(gb2)
        frmbox.addLayout(leftbox)
        frmbox.addLayout(rightbox)
class CGView(QGraphicsView):
    def __init__(self,parent):
        super().__init__(parent)  
        self.scene = QGraphicsScene() 
        self.setScene(self.scene)

        self.items = []
        self.start = QPointF()
        self.end = QPointF()   
class CGView1(QGraphicsView):
    def __init__(self,parent):
        super().__init__(parent)  
        self.scene = QGraphicsScene() 
        self.setScene(self.scene)

        self.items = []
        self.start = QPointF()
        self.end = QPointF()   
        


if __name__== "__main__":
    app = QApplication(sys.argv)
    m = paint()
    sys.exit(app.exec_())


    #곰탕, 설렁탕  카페, 디저트 카페  백숙 삼계탕 옻닭 곱창 막창 양 소곱창 우동 ,소박 냉면 