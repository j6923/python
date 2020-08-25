import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from lastfood import save 

#from ex6 import Figure
class paint(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100,100,1000,900)
        self.setWindowTitle("누가누가 밥사나~~ 진사람이 사지!")
        frmbox = QHBoxLayout()
        self.setLayout(frmbox)
        leftbox = QVBoxLayout()
        rightbox = QVBoxLayout()
        #그룹박스 1 
        gb = QGroupBox("")
        leftbox.addWidget(gb)
        box1 = QVBoxLayout()
        frmbox.addLayout(leftbox)
        frmbox.addLayout(rightbox)
        box1.addLayout(rightbox)
        gb.setLayout(box1)
        box1.addWidget(QRadioButton("한식",self))
        box1.addWidget(QRadioButton("중식",self))
        box1.addWidget(QRadioButton("일식",self))
        box1.addWidget(QRadioButton("양식",self))
        box1.addWidget(QRadioButton("디저트",self))   #triggered 
        
        #그룹박스 2 
        gb1 = QGroupBox("")
        leftbox.addWidget(gb1)
        frmbox.addLayout(leftbox)
        frmbox.addLayout(rightbox)
        box2 = QVBoxLayout()
        gb1.setLayout(box2)
        gb1.setLayout(box2)
        box2.addWidget(QCheckBox("닭볶음탕",self))
        

        box2.addWidget(QCheckBox("곰탕",self))
        box2.addWidget(QCheckBox("설렁탕",self))
        box2.addWidget(QCheckBox("커피",self))
        box2.addWidget(QCheckBox("디저트",self))
        box2.addWidget(QCheckBox("삼계탕",self))
        box2.addWidget(QCheckBox("백숙",self))
        box2.addWidget(QCheckBox("우동",self))
        box2.addWidget(QCheckBox("곱창,막창",self))
        box2.addWidget(QCheckBox("냉면",self))
        box2.addWidget(QCheckBox("커피",self))
        box2.addWidget(QCheckBox("초밥",self))
        box2.addWidget(QCheckBox("모밀",self))
        box2.addWidget(QCheckBox("햄버거",self))
        box2.addWidget(QCheckBox("칼국수",self))
        box2.addWidget(QCheckBox("만두",self))
        box2.addWidget(QCheckBox("짜장면",self))
        box2.addWidget(QCheckBox("빵",self))
        box2.addWidget(QCheckBox("전",self))
        box2.addWidget(QCheckBox("빈대떡",self))
        box2.addWidget(QCheckBox("국수",self))
        box2.addWidget(QCheckBox("수제비",self))
        box2.addWidget(QCheckBox("회",self))
        box2.addWidget(QCheckBox("백반",self))
        box2.addWidget(QCheckBox("태국음식",self))
        box2.addWidget(QCheckBox("스테이크",self))
        box2.addWidget(QCheckBox("파스타",self))
        
        
        #곰탕, 설렁탕  카페, 디저트 카페  백숙 삼계탕 옻닭 곱창 막창 양 소곱창 우동 ,소박 냉면
    # 커피 초밥 롤 정육 냉모밀 햄버거 칼국수 만두 짜장면 빵  
    #전, 빈대떡 국수 수제비 회 백반 가정식  태국음식 스테이크 파스타 피자  
        
        self.view = CGView(self) 
        rightbox.addWidget(self.view) 
        

        self.view = CGView1(self) 
        rightbox.addWidget(self.view) 


        # self.view.clicked.connect(self.save)
    # def dbcheck(self):
    #     connection = #함수로 
        self.show()   

        
    

        # gb2 = QGroupBox("지도")
        # leftbox.addWidget(gb2)
        # frmbox.addLayout(leftbox)
        # frmbox.addLayout(rightbox)
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
    # 커피 초밥 롤 정육 냉모밀 햄버거 칼국수 만두 짜장면 빵  
    #전, 빈대떡 국수 수제비 회 백반 가정식  태국음식 스테이크 파스타 피자    

    #요리주점
    #맥주,호프


    #버튼을 클릭하면 화면에 연결 

    #확인을 누르면 connect  db에 연결해서 